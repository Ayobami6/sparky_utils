from .response import service_response
from .exceptions import handle_internal_server_exception, ServiceException
from functools import wraps
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.http.response import Http404
from rest_framework.exceptions import ValidationError as DRFValidationError


def exception_advice(func) -> any:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ServiceException as e:
            return service_response(
                status="error", message=str(e), status_code=e.status_code
            )
        except ValidationError as e:
            return service_response(status="error", message=str(e), status_code=400)
        except IntegrityError as e:
            return service_response(status="error", message=str(e), status_code=409)
        except Http404 as e:
            return service_response(status="error", message=str(e), status_code=404)
        except DRFValidationError as e:
            if "object does not exist" in str(e.detail):
                return service_response(
                    success=False, message="Resource not found", status_code=404
                )
            return service_response(success=False, message=e.detail, status_code=400)
        except ObjectDoesNotExist as e:
            return service_response(status="error", message=str(e), status_code=404)
        except Exception:
            return handle_internal_server_exception()

    return wrapper

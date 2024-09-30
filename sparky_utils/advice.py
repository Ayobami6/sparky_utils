from .response import service_response
from .exceptions import handle_internal_server_exception, ServiceException
from functools import wraps
from django.core.exceptions import ValidationError, ObjectDoesNotExist


def exception_advice(func) -> any: 
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ServiceException as e:
            return service_response(status="error", message=str(e), status_code=e.status_code)
        except ValidationError as e:
            return service_response(status="error", message=str(e), status_code=400)
        except ObjectDoesNotExist as e:
            return service_response(status="error", message=str(e), status_code=404)
        except Exception:
            return handle_internal_server_exception()
    
    return wrapper
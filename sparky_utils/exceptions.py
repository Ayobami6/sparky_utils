import logging
import traceback
from rest_framework.response import Response
from django.db import models
from datetime import datetime

logger = logging.getLogger(__name__)


def handle_internal_server_exception() -> Response:
    """Handles internal Server error exception

    Returns:
        Response: Http response
    """
    traceback.print_exc()
    logger.error(traceback.format_exc())
    return Response({"status": "error", "message": "Something went wrong"}, status=500)


class SingletonMeta(type):
    """Single meta class"""

    _instances: dict = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class InternalServerExceptionHandler(metaclass=SingletonMeta):

    def __init__(self, model_object):
        if not isinstance(model_object, models.Model):
            raise ValueError("model_object should be an instance of Django model")
        self.model_object = model_object

    def handle_exception(self) -> Response:
        """Handles exception

        Args:
            exception (Exception): Exception object

        Returns:
            Response: Http response
        """
        stack_trace = traceback.format_exc()
        traceback.print_exc()
        logger.error(stack_trace)
        self.model_object.objects.create(
            traceback=stack_trace, timestamp=datetime.now(), severity="ERROR"
        )
        return Response(
            {"status": "error", "message": "Something went wrong", "status_code": 500},
            status=500,
        )


class ServiceException(Exception):
    def __init__(self, status_code, message):
        super().__init__(message)
        self.status_code = status_code
        self.message = message

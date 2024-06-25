import pytest
from unittest.mock import Mock
from rest_framework.response import Response
from sparky_utils.exceptions import (
    handle_internal_server_exception,
)
import logging


def test_handle_internal_server_exception():

    # Act
    response = handle_internal_server_exception()

    # Assert
    assert isinstance(response, Response)
    assert response.status_code == 500
    assert response.data == {"status": "error", "message": "Something went wrong"}

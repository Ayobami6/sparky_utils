import pytest
from rest_framework.response import Response
from sparky_utils.response import service_response  # Replace with the actual module name


def test_service_response_with_empty_data():
    expected_status = "success"
    expected_message = ""
    expected_data = {}
    expected_status_code = 200

    response = service_response(status=expected_status, message=expected_message)

    assert isinstance(response, Response)
    assert response.status_code == expected_status_code
    assert response.data == {
        "status": expected_status,
        "message": expected_message,
        "data": expected_data,
    }


def test_service_response_with_empty_data_and_custom_status():
    expected_status = "custom_status"
    expected_message = ""
    expected_data = {}
    expected_status_code = 200

    response = service_response(status=expected_status, message=expected_message)

    assert isinstance(response, Response)
    assert response.status_code == expected_status_code
    assert response.data == {
        "status": expected_status,
        "message": expected_message,
        "data": expected_data,
    }


def test_service_response_with_empty_data_and_custom_status_code():
    expected_status = "success"
    expected_message = ""
    expected_data = {}
    expected_status_code = 404

    response = service_response(
        status=expected_status,
        message=expected_message,
        status_code=expected_status_code,
    )

    assert isinstance(response, Response)
    assert response.status_code == expected_status_code
    assert response.data == {
        "status": expected_status,
        "message": expected_message,
        "data": expected_data,
    }


def test_service_response_with_empty_data_and_custom_status_and_status_code():
    expected_status = "error"
    expected_message = ""
    expected_data = {}
    expected_status_code = 404

    response = service_response(
        status=expected_status,
        message=expected_message,
        status_code=expected_status_code,
    )

    assert isinstance(response, Response)
    assert response.status_code == expected_status_code
    assert response.data == {
        "status": expected_status,
        "message": expected_message,
        "data": expected_data,
    }


def test_service_response_with_empty_data_and_message():
    expected_status = "success"
    expected_message = "Custom message"
    expected_data = {}
    expected_status_code = 200

    response = service_response(status=expected_status, message=expected_message)

    assert isinstance(response, Response)
    assert response.status_code == expected_status_code
    assert response.data == {
        "status": expected_status,
        "message": expected_message,
        "data": expected_data,
    }

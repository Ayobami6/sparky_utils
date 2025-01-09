from rest_framework.response import Response


def service_response(
    status: str = "success", data: dict = {}, message: str = "", status_code=200
) -> Response:
    """Api response utils functions

    Args:
        status (str, optional): request status Defaults to "success".
        data (dict, optional): response data. Defaults to None.
        message (str, optional): response message. Defaults to None.
        status (int, optional): response status code. Defaults to 200.

    Returns:
        Response: Http response
    """
    data_resp = {
        "status": status,
        "status_code": status_code,
    }
    match status:
        case "success":
            data_resp["data"] = data
            data_resp["message"] = message
        case "error":
            data_resp["message"] = message
        case _:
            data_resp["message"] = message
    if status_code == 204:
        return Response(status=status_code)
    return Response(data=data_resp, status=status_code)

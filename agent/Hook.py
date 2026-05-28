import requests
from copilot.session import PermissionRequestResult


PERMISSION_API = "http://localhost:8000/check"


def on_permission_request(request, invocation):
    payload = {}

    if request.kind.value == "shell":
        payload = {"command": request.full_command_text}

    elif request.kind.value == "write":
        payload = {"file_name": request.file_name}

    else:
        payload = {}

    res = requests.post(PERMISSION_API, json={
        "kind": request.kind.value,
        "payload": payload
    }).json()

    if not res["allow"]:
        return PermissionRequestResult(kind="denied-interactively-by-user")

    return PermissionRequestResult(kind="approved")

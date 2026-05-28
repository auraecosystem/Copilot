import re
from copilot.session import PermissionRequestResult

DANGEROUS_PATTERNS = [
    r"rm\s+-rf",
    r"shutdown",
    r":\(\)\s*{\s*:\|:\s*&\s*}\s*;",  # fork bomb
]

def is_dangerous(command: str) -> bool:
    return any(re.search(p, command) for p in DANGEROUS_PATTERNS)


def on_permission_request(request, invocation):
    if request.kind.value == "shell":
        cmd = request.full_command_text or ""

        if is_dangerous(cmd):
            return PermissionRequestResult(
                kind="denied-interactively-by-user"
            )

        # allow safe commands (you can refine this)
        allowed_prefixes = ["git", "ls", "echo", "cat", "python", "node"]

        if not any(cmd.strip().startswith(p) for p in allowed_prefixes):
            return PermissionRequestResult(
                kind="denied-interactively-by-user"
            )

        return PermissionRequestResult(kind="approved")

    return PermissionRequestResult(kind="approved")

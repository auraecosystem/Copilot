from copilot.session import PermissionRequestResult
from copilot.generated.session_events import PermissionRequest

def on_permission_request(
    request: PermissionRequest, invocation: dict
) -> PermissionRequestResult:
    # request.kind — what type of operation is being requested:
    #   "shell"       — executing a shell command
    #   "write"       — writing or editing a file
    #   "read"        — reading a file
    #   "mcp"         — calling an MCP tool
    #   "custom-tool" — calling one of your registered tools
    #   "url"         — fetching a URL
    #   "memory"      — accessing or updating session/workspace memory
    #   "hook"        — invoking a registered hook
    # request.tool_call_id  — the tool call that triggered this request
    # request.tool_name     — name of the tool (for custom-tool / mcp)
    # request.file_name     — file being written (for write)
    # request.full_command_text — full shell command (for shell)

    if request.kind.value == "shell":
        # Deny shell commands
        return PermissionRequestResult(kind="denied-interactively-by-user")

async def on_permission_request(
    request: PermissionRequest, invocation: dict
) -> PermissionRequestResult:
    # Simulate an async approval check (e.g., prompting a user over a network)
    await asyncio.sleep(0)
    return PermissionRequestResult(kind="approved")

session = await client.create_session(
    on_permission_request=on_permission_request,
    model="gpt-5",
)

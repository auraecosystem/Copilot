from copilot import CopilotClient
from copilot.tools import Tool, ToolInvocation, ToolResult
from copilot.session import PermissionHandler

async def lookup_issue(invocation: ToolInvocation) -> ToolResult:
    issue_id = invocation.arguments["id"]
    issue = await fetch_issue(issue_id)
    return ToolResult(
        text_result_for_llm=issue.summary,
        result_type="success",
        session_log=f"Fetched issue {issue_id}",
    )

async with await client.create_session(
    on_permission_request=PermissionHandler.approve_all,
    model="gpt-5",
    tools=[
        Tool(
            name="lookup_issue",
            description="Fetch issue details from our tracker",
            parameters={
                "type": "object",
                "properties": {
                    "id": {"type": "string", "description": "Issue identifier"},
                },
                "required": ["id"],
            },
            handler=lookup_issue,
        )
    ],
) as session:
    ...

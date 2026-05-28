from pydantic import BaseModel, Field
from copilot import CopilotClient, define_tool

class LookupIssueParams(BaseModel):
    id: str = Field(description="Issue identifier")

@define_tool(description="Fetch issue details from our tracker")
async def lookup_issue(params: LookupIssueParams) -> str:
    issue = await fetch_issue(params.id)
    return issue.summary

async with await client.create_session(
    on_permission_request=PermissionHandler.approve_all,
    model="gpt-5",
    tools=[lookup_issue],
) as session:
    ...

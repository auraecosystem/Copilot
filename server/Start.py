from copilot.session import ElicitationContext, ElicitationResult, PermissionHandler

async def handle_elicitation(
    context: ElicitationContext,
) -> ElicitationResult:
    # context["session_id"]           — the session ID
    # context["message"]              — what the server is asking
    # context.get("requestedSchema")  — optional JSON schema for form fields
    # context.get("mode")             — "form" or "url"

    print(f"Server asks: {context['message']}")

    # Return the user's response
    return {
        "action": "accept",  # or "decline" or "cancel"
        "content": {"answer": "yes"},
    }

async with await client.create_session(
    on_permission_request=PermissionHandler.approve_all,
    on_elicitation_request=handle_elicitation,
) as session:
    ...

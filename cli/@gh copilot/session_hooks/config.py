async def on_pre_tool_use(input, invocation):
    print(f"About to run tool: {input['toolName']}")
    # Return permission decision and optionally modify args
    return {
        "permissionDecision": "allow",  # "allow", "deny", or "ask"
        "modifiedArgs": input.get("toolArgs"),  # Optionally modify tool arguments
        "additionalContext": "Extra context for the model",
    }

async def on_post_tool_use(input, invocation):
    print(f"Tool {input['toolName']} completed")
    return {
        "additionalContext": "Post-execution notes",
    }

async def on_user_prompt_submitted(input, invocation):
    print(f"User prompt: {input['prompt']}")
    return {
        "modifiedPrompt": input["prompt"],  # Optionally modify the prompt
    }

async def on_session_start(input, invocation):
    print(f"Session started from: {input['source']}")  # "startup", "resume", "new"
    return {
        "additionalContext": "Session initialization context",
    }

async def on_session_end(input, invocation):
    print(f"Session ended: {input['reason']}")

async def on_error_occurred(input, invocation):
    print(f"Error in {input['errorContext']}: {input['error']}")
    return {
        "errorHandling": "retry",  # "retry", "skip", or "abort"
    }

async with await client.create_session(
    on_permission_request=PermissionHandler.approve_all,
    model="gpt-5",
    hooks={
        "on_pre_tool_use": on_pre_tool_use,
        "on_post_tool_use": on_post_tool_use,
        "on_user_prompt_submitted": on_user_prompt_submitted,
        "on_session_start": on_session_start,
        "on_session_end": on_session_end,
        "on_error_occurred": on_error_occurred,
    },
) as session:
    ...

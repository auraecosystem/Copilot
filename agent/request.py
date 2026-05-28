async def handle_user_input(request, invocation):
    # request["question"] - The question to ask
    # request.get("choices") - Optional list of choices for multiple choice
    # request.get("allowFreeform", True) - Whether freeform input is allowed

    print(f"Agent asks: {request['question']}")
    if request.get("choices"):
        print(f"Choices: {', '.join(request['choices'])}")

    # Return the user's response
    return {
        "answer": "User's answer here",
        "wasFreeform": True,  # Whether the answer was freeform (not from choices)
    }

async with await client.create_session(
    on_permission_request=PermissionHandler.approve_all,
    model="gpt-5",
    on_user_input_request=handle_user_input,
) as session:
    ...

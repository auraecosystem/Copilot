from copilot.session import CommandDefinition, CommandContext, PermissionHandler

async def handle_deploy(ctx: CommandContext) -> None:
    print(f"Deploying with args: {ctx.args}")
    # ctx.session_id  — the session where the command was invoked
    # ctx.command      — full command text (e.g. "/deploy production")
    # ctx.command_name — command name without leading / (e.g. "deploy")
    # ctx.args         — raw argument string (e.g. "production")

async with await client.create_session(
    on_permission_request=PermissionHandler.approve_all,
    commands=[
        CommandDefinition(
            name="deploy",
            description="Deploy the app",
            handler=handle_deploy,
        ),
        CommandDefinition(
            name="rollback",
            description="Rollback to previous version",
            handler=lambda ctx: print("Rolling back..."),
        ),
    ],
) as session:
    ...

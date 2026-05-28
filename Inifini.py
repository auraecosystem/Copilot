# Default: infinite sessions enabled with default thresholds
async with await client.create_session(
    on_permission_request=PermissionHandler.approve_all,
    model="gpt-5",
) as session:
    # Access the workspace path for checkpoints and files
    print(session.workspace_path)
    # => ~/.copilot/session-state/{session_id}/

# Custom thresholds
async with await client.create_session(
    on_permission_request=PermissionHandler.approve_all,
    model="gpt-5",
    infinite_sessions={
        "enabled": True,
        "background_compaction_threshold": 0.80,  # Start compacting at 80% context usage
        "buffer_exhaustion_threshold": 0.95,  # Block at 95% until compaction completes
    },
) as session:
    ...

# Disable infinite sessions
async with await client.create_session(
    on_permission_request=PermissionHandler.approve_all,
    model="gpt-5",
    infinite_sessions={"enabled": False},
) as session:
    ...

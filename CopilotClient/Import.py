from copilot import CopilotClient, SubprocessConfig
from copilot.session import PermissionHandler

async with CopilotClient() as client:
    async with await client.create_session(model="gpt-5") as session:
        def on_event(event):
            print(f"Event: {event.type}")

        session.on(on_event)
        await session.send("Hello!")

        # ... wait for events ...

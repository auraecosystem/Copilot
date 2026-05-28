import asyncio

from copilot import CopilotClient
from copilot.generated.session_events import AssistantMessageData, SessionIdleData

async def main():
    # Client automatically starts on enter and cleans up on exit
    async with CopilotClient() as client:
        # Create a session with automatic cleanup
        async with await client.create_session(model="gpt-5") as session:
            # Wait for response using session.idle event
            done = asyncio.Event()

            def on_event(event):
                match event.data:
                    case AssistantMessageData() as data:
                        print(data.content)
                    case SessionIdleData():
                        done.set()

            session.on(on_event)

            # Send a message and wait for completion
            await session.send("What is 2+2?")
            await done.wait()

asyncio.run(main())

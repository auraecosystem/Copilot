Build a creative realtime audio app called "World Room" using the current OpenAI Realtime API.

The experience should let a user speak with a live worldbuilding companion that helps invent settings, characters, conflicts, and scene hooks. Audio should be central to the experience, with low-latency turn-taking and a playful voice interaction model.

Requirements:

- Use the current Realtime API patterns for low-latency audio, not a request/response text-only loop.
- Support audio input and output, and include text transcript display if practical.
- Clearly separate browser/client responsibilities from server/session-token responsibilities.
- Include setup steps for OPENAI_API_KEY and local development.
- Add developer notes for latency, session lifecycle, permissions, and error recovery.
- Keep the UI focused and polished with obvious microphone/session states.
- Include a validation checklist for testing audio permissions, connection recovery, and basic conversation quality.

Documentation:

- If the OpenAI Docs skill is available, use it to verify the latest OpenAI API guidance before implementing.
- If the OpenAI Docs skill is not available, install the OpenAI Docs skill and use it.
- If the OpenAI Docs skill cannot be installed or used, use web search to search the latest OpenAI developer documentation on developers.openai.com/api.
- Reference https://developers.openai.com/api/docs/models for guidance on the latest models to use.

Frontend:

- If the Frontend skill is installed, use it for frontend implementation and polish.
- If the Frontend skill is not installed, install the Frontend skill and use it.

Inspect this repository's OpenAI integration and create a plan to upgrade to the latest recommended model and API patterns for this app. Do not change code.

Please:

- Find all OpenAI SDK calls, model names, prompt construction, streaming paths, structured outputs, tool usage, and tests.
- Identify outdated model usage or legacy API patterns.
- Recommend the safest current API path for this app, such as Responses API for general multimodal/tool-using workflows, Agents SDK for agentic orchestration, or Realtime API for low-latency voice experiences.
- Produce a step-by-step implementation plan that preserves behavior and public interfaces where possible.
- Flag risky changes, compatibility concerns, and areas that need manual review.
- Recommend the tests, fixtures, and docs that should be added or updated.
- Finish with a concise migration plan, risk notes, and a validation plan I can run locally.

Documentation:

- If the OpenAI Docs skill is available, use it to verify the latest OpenAI API guidance before implementing.
- If the OpenAI Docs skill is not available, install the OpenAI Docs skill and use it.
- If the OpenAI Docs skill cannot be installed or used, use web search to search the latest OpenAI developer documentation on developers.openai.com/api.
- Reference https://developers.openai.com/api/docs/models for guidance on the latest models to use.

Frontend:

- If the Frontend skill is installed, use it for frontend implementation and polish.
- If the Frontend skill is not installed, install the Frontend skill and use it.

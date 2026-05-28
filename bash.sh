npm install -g @github/copilot
pip install -e ".[telemetry,dev]"
# or
uv pip install -e ".[telemetry,dev]"
npx skills add https://github.com/cloudflare/skills
  curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_GITHUB_PAT" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  -H "Content-Type: application/json" \
  https://models.github.ai/inference/chat/completions \
  -d '{"model":"gpt-5","messages":[{"role":"user","content":"What is the capital of France?"}]}'

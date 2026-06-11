# core_engine.py
import re, time, hashlib
from dataclasses import dataclass

class Risk:
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Decision:
    allow: bool
    risk: str
    reason: str


class PermissionEngine:
    def __init__(self):
        self.logs = []

        self.danger_shell = [
            r"rm\s+-rf",
            r"mkfs",
            r"dd\s+if=",
            r":\(\)\s*{\s*:\|:\s*&\s*}",
        ]

        self.allowed_shell = ["git", "ls", "echo", "cat", "python", "node", "go", "npm"]

    def shell(self, cmd: str) -> Decision:
        if any(re.search(p, cmd) for p in self.danger_shell):
            return Decision(False, Risk.HIGH, "Dangerous shell pattern")

        if not any(cmd.startswith(p) for p in self.allowed_shell):
            return Decision(False, Risk.MEDIUM, "Not in allowlist")

        return Decision(True, Risk.LOW, "Safe shell")

    def write(self, file_name: str) -> Decision:
        if any(x in file_name for x in ["/etc", ".ssh", "id_rsa"]):
            return Decision(False, Risk.HIGH, "Protected system file")

        return Decision(True, Risk.MEDIUM, "Workspace write allowed")

    def hash_event(self, event: dict) -> str:
        raw = str(event).encode()
        return hashlib.sha256(raw).hexdigest()

    def log(self, request, decision: Decision):
        event = {
            "time": time.time(),
            "kind": request.kind.value,
            "tool": getattr(request, "tool_name", None),
            "decision": decision.__dict__,
        }
        event["hash"] = self.hash_event(event)
        self.logs.append(event)
        return event

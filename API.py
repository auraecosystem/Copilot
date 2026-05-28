# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from core_engine import PermissionEngine, Decision, Risk

app = FastAPI()
engine = PermissionEngine()


class PermissionRequest(BaseModel):
    kind: str
    payload: dict


@app.post("/check")
def check_permission(req: PermissionRequest):
    kind = req.kind
    payload = req.payload

    if kind == "shell":
        decision = engine.shell(payload.get("command", ""))

    elif kind == "write":
        decision = engine.write(payload.get("file_name", ""))

    else:
        decision = Decision(True, Risk.LOW, "Default allow")

    log = engine.log(req, decision)

    return {
        "allow": decision.allow,
        "risk": decision.risk,
        "reason": decision.reason,
        "event_hash": log["hash"],
    }


@app.get("/logs")
def logs():
    return engine.logs

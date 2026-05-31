package privacy

default allow = false

# Input shape:
# {
#   "user": {"id": "...", "role": "admin", "clearance": 3},
#   "action": "read" | "delete" | "export" | "grant",
#   "resource": {"type": "file", "class": 0-3, "owner": "..."},
#   "context": {"mfa": true, "device_trusted": true, "time": "13:10"},
#   "approvals": 0|1|2
# }

# Least privilege
allow {
  input.user.role == "admin"
  input.user.clearance >= input.resource.class
  input.context.mfa
  input.context.device_trusted
}

# Dual control for risky actions
allow {
  input.action == "delete" or input.action == "export" or input.action == "grant"
  input.user.role == "admin"
  input.approvals >= 2
  input.context.mfa
}

# Deny off-hours for high sensitivity
deny[msg] {
  input.resource.class >= 2
  t := time.now_ns()
  hour := time.hour(t)
  hour < 6 or hour > 22
  msg := "Off-hours access blocked"
}

# Explicit allow overrides default deny

"""Validate the actual Compose model without resolving runtime secrets or a daemon."""
import json
import os
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
deployment = root / "deploy/postiz"
env = dict(os.environ, POSTIZ_ROOT="/assigned/postiz")
result = subprocess.run(
    ["docker", "compose", "--env-file", str(deployment / "images.env"),
     "-f", str(deployment / "compose.yml"), "--profile", "operations",
     "config", "--no-env-resolution",
     "--no-path-resolution", "--format", "json"],
    env=env, capture_output=True, text=True, check=True,
)
model = json.loads(result.stdout)
services = model["services"]
assert len(services) == 8
for name, service in services.items():
    assert not service.get("ports"), f"Published port: {name}"
    assert re.fullmatch(r".+@sha256:[0-9a-f]{64}", service["image"]), name
    assert service["restart"] == "unless-stopped", name
    assert not service.get("privileged"), name
    for volume in service.get("volumes", []):
        assert volume["type"] == "bind", name
        assert volume["source"].startswith("/assigned/postiz/state/") or volume["read_only"], name
    if "edge" in service["networks"]:
        assert name == "postiz"
assert model["networks"]["workflow"]["internal"]
assert model["networks"]["edge"]["external"]
app = services["postiz"]["environment"]
assert app["DISABLE_REGISTRATION"] == "true"
assert app["FRONTEND_URL"] == app["MAIN_URL"] == "https://social.wlkrlabs.com"
assert app["NEXT_PUBLIC_BACKEND_URL"] == "https://social.wlkrlabs.com/api"
assert app["BACKEND_INTERNAL_URL"] == "http://localhost:3000"
assert app["TEMPORAL_ADDRESS"] == "temporal:7233"
assert app["STORAGE_PROVIDER"] == "local"
assert app["EMAIL_SECURE"] == "true"
assert not any(key in app for key in (
    "NOT_SECURED", "DISABLE_SSRF_PROTECTION", "STRIPE_PUBLISHABLE_KEY",
    "OPENAI_API_KEY", "X_API_KEY", "TIKTOK_CLIENT_ID", "PINTEREST_CLIENT_ID",
))
assert services["temporal-ui"]["profiles"] == ["operations"]
assert services["temporal-admin-tools"]["profiles"] == ["operations"]
for script in (deployment / "project", *deployment.glob("*.sh")):
    subprocess.run(["bash", "-n", str(script)], check=True)
print("PASS: pinned upstream services, private ports/networks, persistent binds, production settings and shell syntax")

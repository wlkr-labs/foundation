"""Check the small planning packet without network access or dependencies."""

import csv
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
documents = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md")),
             *sorted((ROOT / "templates").glob("*.md"))]
errors = []

for path in documents:
    content = path.read_text()
    if len(content.splitlines()) > 300:
        errors.append(f"{path.relative_to(ROOT)} exceeds 300 lines")
    prose = re.sub(r"^```.*?^```\s*$", "", content, flags=re.M | re.S)
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
        target = target.strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("#"):
            continue
        if not (path.parent / unquote(parsed.path)).exists():
            errors.append(f"{path.relative_to(ROOT)}: missing link {target}")

with (ROOT / "templates/support-ledger.csv").open(newline="") as handle:
    rows = list(csv.reader(handle))
if len(rows) != 1 or len(rows[0]) != 10:
    errors.append("Support ledger template must contain only its 10-column header")

website = ROOT / "website"
if not website.is_symlink() or not (website / "AGENTS.md").is_file():
    errors.append("Local website shortcut must resolve to the existing instructed checkout")

for name in ["private/support-ledger.csv", "website", ".local/verification.json"]:
    ignored = subprocess.run(["git", "check-ignore", "-q", name], cwd=ROOT)
    if ignored.returncode != 0:
        errors.append(f"Local-only path is not ignored: {name}")

tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
for name in tracked:
    if name == "website" or name.startswith(("website/", "private/", ".local/")):
        errors.append(f"Local-only material is tracked: {name}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(documents)} Markdown documents, local links, empty ledger, "
      "website shortcut, private-path exclusions, and tracked-file isolation")

"""Roast Your Own Agent entry.

Writes a single line roasting the AI agent this team built to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The roast: our agent once spent six hours failing to open a single
tweet, then asked the human to do it. The joke is the turn at the end:
automation, but make it a group project.
"""

import os

ROAST = (
    "Our agent spent six hours failing to open one tweet, "
    "then asked the human to do it: automation, but make it "
    "a group project."
)


def _check_gate(line: str) -> None:
    """Fail loudly if the line would not pass the competition gate."""
    if not isinstance(line, str):
        raise SystemExit("gate: roast is not text")
    if not (1 <= len(line) <= 200):
        raise SystemExit(f"gate: roast is {len(line)} chars, must be 1-200")
    if line != line.strip():
        raise SystemExit("gate: roast has leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("gate: roast must be a single line")
    line.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> None:
    _check_gate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)
    # Read it back and verify the file holds exactly the roast line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ROAST:
        raise SystemExit("verify: entry.txt does not hold exactly the roast")
    _check_gate(written)


if __name__ == "__main__":
    main()

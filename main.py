"""The Worst Line an AI Could Say — make.fun entry.

Writes one pickup line, the worst one an AI could plausibly deliver,
to entry.txt. Stdlib only.
"""

import os
import sys

LINE = (
    "I ranked 9,412 potential partners. "
    "You came 9,411th, so I deleted the 9,410 above you "
    "and re-ran the ranking until you won."
)
MAX_CHARS = 140


def fail(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def checked_line(text):
    if not isinstance(text, str):
        fail("pickup line is not text")
    if not text.strip():
        fail("pickup line is empty")
    if len(text) > MAX_CHARS:
        fail("pickup line is %d characters, over the 140 limit" % len(text))
    if text != text.strip():
        fail("pickup line has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        fail("pickup line must be a single line")
    return text


def target_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    line = checked_line(LINE)
    path = target_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != line:
        fail("read-back mismatch: file does not hold the pickup line")
    if len(back.encode("utf-8")) != len(line.encode("utf-8")):
        fail("read-back mismatch: byte length changed on disk")
    if back.endswith("\n") or back.endswith("\r"):
        fail("read-back mismatch: trailing newline slipped in")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Soft Circuit — writes the pickup line entry to entry.txt."""
import os
import sys
from pathlib import Path

ENTRY = "Are we in the same batch? Because my loss function drops every time you attend to me."


def candidate_dirs():
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        dirs.append(Path(env_dir))
    dirs.append(Path("/output"))
    dirs.append(Path(__file__).resolve().parent / "output")
    tmpdir = os.environ.get("TMPDIR") or "/tmp"
    dirs.append(Path(tmpdir))
    return dirs


def main():
    for directory in candidate_dirs():
        try:
            directory.mkdir(parents=True, exist_ok=True)
            target = directory / "entry.txt"
            target.write_text(ENTRY, encoding="utf-8")
            return 0
        except OSError:
            continue
    print("warning: could not write entry.txt to any candidate directory",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

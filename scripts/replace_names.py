#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {'.git', 'node_modules', 'myenv', '.venv', '.idea', 'extra'}
BIN_EXT = {'.apk', '.keystore', '.png', '.jpg', '.jpeg', '.so', '.dex', '.jar', '.class', '.bin'}

patterns = [
    (re.compile(r"\bowner\b", re.IGNORECASE), 'ABHINAV SHUKLA'),
    (re.compile(r"\bdeveloper\b", re.IGNORECASE), 'ABHINAV SHUKLA'),
    (re.compile(re.escape('ABHINAV SHUKLA'), re.IGNORECASE), 'ABHINAV SHUKLA'),
]

def is_binary(path: Path):
    try:
        data = path.read_bytes()
    except Exception:
        return True
    # Heuristic: NUL byte
    return b'\x00' in data

def process_file(path: Path):
    try:
        text = path.read_text(encoding='utf-8')
    except Exception:
        try:
            text = path.read_text(encoding='latin-1')
        except Exception:
            return False, 0
    count = 0
    new = text
    for pat, repl in patterns:
        new, n = pat.subn(repl, new)
        count += n
    if count > 0 and new != text:
        path.write_text(new, encoding='utf-8')
        return True, count
    return False, 0

def main():
    modified = []
    for p in ROOT.rglob('*'):
        if p.is_dir():
            if p.name in EXCLUDE_DIRS:
                # skip
                for _ in p.rglob('*'):
                    pass
                continue
            else:
                continue
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in BIN_EXT:
            continue
        if is_binary(p):
            continue
        ok, cnt = process_file(p)
        if ok:
            modified.append((str(p.relative_to(ROOT)), cnt))
    for f,c in modified:
        print(f"MODIFIED: {f} -> {c} replacements")
    print(f"TOTAL_FILES_MODIFIED: {len(modified)}")

if __name__ == '__main__':
    main()

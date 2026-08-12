#!/usr/bin/env python3
from zipfile import ZipFile, ZipInfo
from pathlib import Path
import re
import shutil

SRC = Path('SATAN.apk')
OUT = Path('SATAN_rebranded.apk')

# Byte patterns to replace (must be same length when ASCII)
replacements = [
    # package name ascii (18 bytes) -> keep length same
    (b'com.brahma.connect', b'com.satanx.connect'),
    # simple brand token (6 bytes) -> keep length same
    (b'brahma', b'satanx'),
]

# Also replace UTF-16LE/BE occurrences
def enc_repls(pat_ascii, repl_ascii):
    return [
        (pat_ascii, repl_ascii),
        (pat_ascii.decode('ascii').encode('utf-16le'), repl_ascii.decode('ascii').encode('utf-16le')),
        (pat_ascii.decode('ascii').encode('utf-16be'), repl_ascii.decode('ascii').encode('utf-16be')),
    ]

all_repl = []
for a,b in replacements:
    all_repl.extend(enc_repls(a,b))

def apply_replacements(data):
    out = data
    for pat, repl in all_repl:
        if pat in out:
            out = out.replace(pat, repl)
    return out

def new_entry_name(name: str) -> str:
    # rename files containing brahma -> satanx in path
    return name.replace('brahma', 'satanx')

def main():
    if not SRC.exists():
        print('Source APK not found:', SRC)
        return
    if OUT.exists():
        OUT.unlink()
    with ZipFile(SRC, 'r') as zin, ZipFile(OUT, 'w') as zout:
        for zinfo in zin.infolist():
            data = zin.read(zinfo.filename)
            # apply replacements to file content for relevant files
            if any(zinfo.filename.endswith(ext) for ext in ('.xml', '.arsc', '.dex', '.mf', '.txt')) or b'brahma' in data or b'com.brahma' in data:
                data = apply_replacements(data)
            # compute new filename
            newname = new_entry_name(zinfo.filename)
            # preserve compression
            zi = ZipInfo(newname)
            zi.compress_type = zinfo.compress_type
            zi.external_attr = zinfo.external_attr
            zi.date_time = zinfo.date_time
            zout.writestr(zi, data)
    print('Wrote', OUT)

if __name__ == '__main__':
    main()

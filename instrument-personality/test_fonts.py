# -*- coding: utf-8 -*-
# Check if TTF files are valid
import os, sys

font_dir = r'C:\Users\32047\lobsterai\project\instrument-personality\fonts'
for fn in os.listdir(font_dir):
    path = os.path.join(font_dir, fn)
    with open(path, 'rb') as f:
        magic = f.read(4)
    size = os.path.getsize(path)
    valid = magic in [b'\x00\x01\x00\x00', b'OTTO', b'true', b'typ1']
    print(fn, '-', 'OK' if valid else 'BAD', '-', size, 'bytes')
# -*- coding: utf-8 -*-
import struct, os

src = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal.png'
with open(src, 'rb') as f:
    data = f.read()

print(f'File size: {len(data)} bytes')
pos = 8
while pos < len(data):
    length = struct.unpack('>I', data[pos:pos+4])[0]
    chunk_type = data[pos+4:pos+8]
    print(f'  {chunk_type.decode("latin-1", errors="replace")}: len={length}')
    pos += 12 + length
# -*- coding: utf-8 -*-
import struct, os

src = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal.png'
with open(src, 'rb') as f:
    data = f.read()

print(f'File size: {len(data)} bytes')
print(f'Magic: {data[:8].hex()}')

pos = 8
chunk_num = 0
while pos < len(data):
    if pos + 4 > len(data):
        print(f'pos {pos}: not enough for length')
        break
    length = struct.unpack('>I', data[pos:pos+4])[0]
    if pos + 8 > len(data):
        print(f'pos {pos}: not enough for chunk header')
        break
    chunk_type = data[pos+4:pos+8].decode('latin-1', errors='replace')
    print(f'Chunk {chunk_num}: {chunk_type}, length={length}, pos={pos}')
    chunk_num += 1
    if chunk_type == 'IEND':
        break
    pos += 12 + length
    if chunk_num > 20:
        print('Too many chunks')
        break
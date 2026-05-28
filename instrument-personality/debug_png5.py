# -*- coding: utf-8 -*-
import zlib, struct, os

src = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal.png'

with open(src, 'rb') as f:
    data = f.read()

# Parse all chunks
pos = 8
chunks = {}
while pos < len(data):
    length = struct.unpack('>I', data[pos:pos+4])[0]
    chunk_type = data[pos+4:pos+8]
    chunk_data = data[pos+8:pos+8+length]
    if chunk_type in chunks:
        chunks[chunk_type] += chunk_data
    else:
        chunks[chunk_type] = chunk_data
    pos += 12 + length

w, h = 414, 430

# Try decompression with zlib
raw = zlib.decompress(chunks[b'IDAT'])
total = len(raw)
print(f'Decompressed: {total} bytes for {w}x{h} image')

# Try different strides
for stride in [w*3+1, w*3, w*4+1, w*4]:
    rows = total // stride
    print(f'  stride={stride}: {rows} complete rows')

# Also try with raw deflate (wbits=-15)
raw2 = zlib.decompress(chunks[b'IDAT'], -15)
print(f'Decompressed (-15): {len(raw2)} bytes')
for stride in [w*3+1, w*3, w*4+1, w*4]:
    rows = len(raw2) // stride
    print(f'  stride={stride}: {rows} rows')
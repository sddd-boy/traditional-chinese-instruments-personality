# -*- coding: utf-8 -*-
import zlib, struct, os

src = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal.png'

with open(src, 'rb') as f:
    data = f.read()

pos = 8
chunks = {}
while pos < len(data):
    length = struct.unpack('>I', data[pos:pos+4])[0]
    chunk_type_bytes = data[pos+4:pos+8]
    chunk_data = data[pos+8:pos+8+length]
    chunk_type_str = chunk_type_bytes.decode('latin-1', errors='replace')
    key = chunk_type_str.encode('latin-1')
    if key in chunks:
        chunks[key] += chunk_data
    else:
        chunks[key] = chunk_data
    pos += 12 + length

ihdr = chunks.get(b'IHDR', b'')
print(f'IHDR len: {len(ihdr)} bytes')
print(f'IHDR hex (first 20): {ihdr[:20].hex()}')
if len(ihdr) >= 13:
    w, h, bitd, ctype, comp, filt, inter = struct.unpack('>IIBBBBB', ihdr[:13])
    print(f'Size: {w}x{h}, bitd={bitd}, ctype={ctype}')

idat = chunks[b'IDAT']
print(f'IDAT total len: {len(idat)}')
try:
    raw = zlib.decompress(idat)
    print(f'Decompressed raw: {len(raw)} bytes')
except Exception as e:
    print(f'Decompress failed: {e}')
    # Try concatenating all IDAT chunks first
    raw2 = zlib.decompress(idat, -15)
    print(f'Decompressed (raw): {len(raw2)}')
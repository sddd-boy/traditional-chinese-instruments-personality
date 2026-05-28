# -*- coding: utf-8 -*-
import zlib, struct, os

def read_png_chunks(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    pos = 8
    chunks = {}
    while pos < len(data):
        length = struct.unpack('>I', data[pos:pos+4])[0]
        chunk_type = data[pos+4:pos+8]
        chunk_data = data[pos+8:pos+8+length]
        pos += 12 + length
        chunks[chunk_type] = chunk_data
    return chunks

def parse_ihdr(data):
    return struct.unpack('>IIBBBBB', data)

src = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal.png'
chunks = read_png_chunks(src)
w, h, bitd, ctype, comp, filt, inter = parse_ihdr(chunks[b'IHDR'])
print(f'Size: {w}x{h}, bitd={bitd}, ctype={ctype}')
print(f'Compression: {comp}, Filter: {filt}, Interlace: {inter}')

idat_data = chunks[b'IDAT']
print(f'IDAT size: {len(idat_data)}')

# Try different wbits values
for wbits in [15, -15, 31, -31, 0, 9, 27]:
    try:
        decompressed = zlib.decompress(idat_data, wbits)
        print(f'wbits={wbits}: SUCCESS, decompressed size = {len(decompressed)}')
        print(f'Expected: {h * (1 + w * 4)} (for RGBA, no interlacing)')
        break
    except Exception as e:
        print(f'wbits={wbits}: FAILED - {e}')
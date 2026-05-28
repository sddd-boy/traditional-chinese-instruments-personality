# -*- coding: utf-8 -*-
import zlib, struct, os

src = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal.png'
dst = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal-nobg.png'

with open(src, 'rb') as f:
    data = f.read()

# Parse PNG chunks
pos = 8
chunks = {}
while pos < len(data):
    length = struct.unpack('>I', data[pos:pos+4])[0]
    chunk_type = data[pos+4:pos+8]
    chunk_data = data[pos+8:pos+8+length]
    if chunk_type in chunks:
        chunks[chunk_type] = chunks[chunk_type] + chunk_data
    else:
        chunks[chunk_type] = chunk_data
    pos += 12 + length

# Parse IHDR - get first 13 bytes
ihdr_full = chunks[b'IHDR']
w = struct.unpack('>I', ihdr_full[0:4])[0]
h = struct.unpack('>I', ihdr_full[4:8])[0]
bitd = ihdr_full[8]
ctype = ihdr_full[9]
bpp = 3 if ctype == 2 else 4
print(f'Image: {w}x{h}, bpp={bpp}')

raw = zlib.decompress(chunks[b'IDAT'])
print(f'Decompressed raw: {len(raw)} bytes')

def sub_filter(row, bpp):
    out = bytearray(row)
    for i in range(bpp, len(row)):
        out[i] = (row[i] + out[i-bpp]) & 0xff
    return bytes(out)

def up_filter(row, prev):
    if not prev:
        return row
    return bytes((row[i] + prev[i]) & 0xff for i in range(len(row)))

def paeth_pred(a, b, c):
    p = a + b - c
    pa = abs(a - p)
    pb = abs(b - p)
    pc = abs(c - p)
    if pa <= pb and pa <= pc:
        return a
    elif pb <= pc:
        return b
    else:
        return c

def paeth_filter(row, prev, bpp):
    if not prev:
        prev = b'\x00' * len(row)
    out = bytearray(len(row))
    for i in range(len(row)):
        left = out[i-bpp] if i >= bpp else 0
        up = prev[i]
        up_left = prev[i-bpp] if i >= bpp else 0
        out[i] = (row[i] + paeth_pred(left, up, up_left)) & 0xff
    return bytes(out)

rows_raw = []
pos = 0
prev_row = b'\x00' * w * bpp
for y in range(h):
    ft = raw[pos]
    pos += 1
    row = raw[pos:pos + w * bpp]
    pos += w * bpp
    if ft == 0:
        pass
    elif ft == 1:
        row = sub_filter(row, bpp)
    elif ft == 2:
        row = up_filter(row, prev_row)
    elif ft == 4:
        row = paeth_filter(row, prev_row, bpp)
    prev_row = row
    rows_raw.append(row)

print(f'Parsed {len(rows_raw)} rows')

# White to transparent
new_rows = []
for y in range(h):
    row = rows_raw[y]
    nr = bytearray(w * 4)
    for x in range(w):
        r = row[x*bpp]
        g = row[x*bpp+1]
        b = row[x*bpp+2]
        if r > 220 and g > 220 and b > 220:
            nr[x*4:x*4+4] = [0, 0, 0, 0]
        else:
            nr[x*4:x*4+4] = [r, g, b, 255]
    new_rows.append(bytes(nr))

def mkchunk(t, d):
    crc = zlib.crc32(t + d) & 0xffffffff
    return struct.pack('>I', len(d)) + t + d + struct.pack('>I', crc)

ihdr_new = struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0)
raw_out = b''.join(b'\x00' + new_rows[y] for y in range(h))
compressed = zlib.compress(raw_out, 9)

png_out = b'\x89PNG\r\n\x1a\n'
png_out += mkchunk(b'IHDR', ihdr_new)
png_out += mkchunk(b'IDAT', compressed)
png_out += mkchunk(b'IEND', b'')

with open(dst, 'wb') as f:
    f.write(png_out)
print(f'Saved: {dst} ({os.path.getsize(dst)} bytes)')
# -*- coding: utf-8 -*-
# Pure Python PNG background remover (white -> transparent)
# Only uses built-in modules: zlib, struct, io

import zlib, struct, io, os

def read_png(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    # Parse PNG signature
    signature = data[:8]
    if signature != b'\x89PNG\r\n\x1a\n':
        raise ValueError('Not a PNG file')
    pos = 8
    chunks = {}
    while pos < len(data):
        length = struct.unpack('>I', data[pos:pos+4])[0]
        chunk_type = data[pos+4:pos+8]
        chunk_data = data[pos+8:pos+8+length]
        crc = struct.unpack('>I', data[pos+8+length:pos+12+length])[0]
        chunks[chunk_type] = chunk_data
        pos += 12 + length
    return chunks

def parse_ihdr(data):
    w, h, bitd, ctype, comp, filt, inter = struct.unpack('>IIBBBBB', data)
    return w, h, bitd, ctype

def deflate_uncompress(compressed):
    return zlib.decompress(compressed, -15)

def adler32_checksum(data):
    return zlib.adler32(data) & 0xffffffff

def apply_filter(row, prev_row, filter_type):
    if filter_type == 0:  # None
        return list(row)
    elif filter_type == 1:  # Sub
        result = list(row)
        for i in range(3, len(row)):
            result[i] = (row[i] + result[i-3]) & 0xff
        return result
    elif filter_type == 2:  # Up
        if not prev_row:
            return list(row)
        result = []
        for i in range(len(row)):
            result.append((row[i] + prev_row[i]) & 0xff)
        return result
    elif filter_type == 3:  # Average
        result = list(row)
        for i in range(len(row)):
            left = result[i-3] if i >= 3 else 0
            up = prev_row[i] if prev_row else 0
            result[i] = (row[i] + (left + up) // 2) & 0xff
        return result
    elif filter_type == 4:  # Paeth
        result = list(row)
        for i in range(len(row)):
            left = result[i-3] if i >= 3 else 0
            up = prev_row[i] if prev_row else 0
            up_left = prev_row[i-3] if (prev_row and i >= 3) else 0
            p = left + up - up_left
            pa = abs(left - up_left)
            pb = abs(up - up_left)
            pc = abs(left + up - 2*up_left)
            pred = left if pa <= pb and pa <= pc else (up if pb <= pc else up_left)
            result[i] = (row[i] + pred) & 0xff
        return result
    return list(row)

def make_white_transparent(png_path, out_path, threshold=230):
    chunks = read_png(png_path)
    ihdr_data = chunks[b'IHDR']
    w, h, bitd, ctype = parse_ihdr(ihdr_data)
    
    # Only support 8-bit RGB or RGBA
    if ctype == 2:  # RGB
        bytes_per_pixel = 3
    elif ctype == 6:  # RGBA
        bytes_per_pixel = 4
    else:
        raise ValueError(f'Unsupported color type: {ctype}')
    
    compressed = chunks[b'IDAT']
    raw_data = deflate_uncompress(compressed)
    
    # Decompose raw data into rows
    rows = []
    pos = 0
    prev_row = b'\x00' * (w * bytes_per_pixel)
    for y in range(h):
        filter_type = raw_data[pos]; pos += 1
        row_bytes = raw_data[pos:pos + w * bytes_per_pixel]; pos += w * bytes_per_pixel
        prev_row = apply_filter(row_bytes, prev_row, filter_type)
        rows.append(bytes(prev_row))
    
    # Process: convert white pixels to transparent
    new_rows = []
    for y in range(h):
        row = rows[y]
        new_row = bytearray(w * 4)  # RGBA output
        for x in range(w):
            if bytes_per_pixel == 3:
                r, g, b = row[x*3], row[x*3+1], row[x*3+2]
                a = 255
            else:
                r, g, b, a = row[x*4], row[x*4+1], row[x*4+2], row[x*4+3]
            
            # If pixel is white-ish and somewhat opaque, make transparent
            if r > threshold and g > threshold and b > threshold and a > 10:
                new_row[x*4:x*4+4] = [0, 0, 0, 0]
            else:
                new_row[x*4:x*4+4] = [r, g, b, 255]
        new_rows.append(bytes(new_row))
    
    # Re-compress with zlib
    raw_out = b''
    prev_row = b'\x00' * (w * 4)
    for y in range(h):
        raw_out += b'\x00'  # filter type 0 (None)
        raw_out += new_rows[y]
    
    compressed_out = zlib.compress(raw_out, 9)
    
    # Build output PNG
    def make_chunk(chunk_type, data):
        crc = zlib.crc32(chunk_type + data) & 0xffffffff
        return struct.pack('>I', len(data)) + chunk_type + data + struct.pack('>I', crc)
    
    # IHDR: RGBA
    ihdr_new = struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0)
    
    png_out = b'\x89PNG\r\n\x1a\n'
    png_out += make_chunk(b'IHDR', ihdr_new)
    png_out += make_chunk(b'IDAT', compressed_out)
    png_out += make_chunk(b'IEND', b'')
    
    with open(out_path, 'wb') as f:
        f.write(png_out)
    print(f'Saved: {out_path} ({os.path.getsize(out_path)} bytes)')

src = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal.png'
dst = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal-nobg.png'
make_white_transparent(src, dst, threshold=220)
print('Done')
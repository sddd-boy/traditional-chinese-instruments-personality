# -*- coding: utf-8 -*-
import struct

def read_jpeg_dim(path):
    with open(path, 'rb') as f:
        data = f.read()
    i = 0
    while i < len(data) - 1:
        if data[i] == 0xFF:
            marker = data[i+1]
            if marker in (0xC0, 0xC1, 0xC2):
                h = struct.unpack('>H', data[i+5:i+7])[0]
                w = struct.unpack('>H', data[i+7:i+9])[0]
                return w, h
            length = struct.unpack('>H', data[i+2:i+4])[0]
            i += 2 + length
        else:
            i += 1
    return None, None

path = r'C:\Users\32047\lobsterai\project\instrument-personality'
instruments = ['erhu', 'pipa', 'guqin', 'dizi', 'guzheng', 'suona']

for inst in instruments:
    fpath = path + '\\bg-result-' + inst + '.jpg'
    w, h = read_jpeg_dim(fpath)
    print(f'{inst}: {w}x{h}')
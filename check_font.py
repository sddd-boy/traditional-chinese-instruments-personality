# -*- coding: utf-8 -*-
from fontTools.ttLib import TTFont
import os

font_path = r'C:\Users\32047\lobsterai\project\instrument-personality\fonts\MaShanZheng.ttf'
try:
    font = TTFont(font_path)
    print('Tables:', list(font.keys())[:20])
    name_table = font['name']
    print('\nName records:')
    for record in name_table.names:
        if record.nameID in [1, 4, 5, 6]:
            try:
                print(f'  nameID={record.nameID} platform={record.platformID} platEnc={record.platEncID} lang={record.langID} => {record.toUnicode()}')
            except:
                print(f'  nameID={record.nameID} platform={record.platformID} platEnc={record.platEncID} lang={record.langID} => [bytes]')
except Exception as e:
    print('fontTools not available:', e)
    # Try reading raw bytes
    with open(font_path, 'rb') as f:
        data = f.read(10000)
    text = data.decode('latin-1', errors='replace')
    import re
    # Look for name records
    for match in re.finditer(r'b'(name|post|cmap)', text[:5000]):
        print(match.group())
    print('File size:', os.path.getsize(font_path))
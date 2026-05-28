# -*- coding: utf-8 -*-
import urllib.request
import os

font_dir = r'C:\Users\32047\lobsterai\project\instrument-personality\fonts'
os.makedirs(font_dir, exist_ok=True)

fonts = {
    'MaShanZheng-Regular.ttf': 'https://github.com/googlefonts/mashanzheng/raw/main/fonts/ttf/MaShanZheng-Regular.ttf',
    'ZCOOLKuaiLe-Regular.ttf': 'https://github.com/fontself/ZCOOLKuaiLe/raw/master/fonts/ZCOOLKuaiLe-Regular.ttf',
}

for filename, url in fonts.items():
    path = os.path.join(font_dir, filename)
    if os.path.exists(path):
        print(f'SKIP (exists): {filename}')
        continue
    try:
        urllib.request.urlretrieve(url, path)
        print(f'DOWNLOADED: {filename} ({os.path.getsize(path)} bytes)')
    except Exception as e:
        print(f'FAILED: {filename} - {e}')

print('Done')
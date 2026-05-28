# -*- coding: utf-8 -*-
import os

path = r'C:\Users\32047\lobsterai\project\instrument-personality'

# Step 1: Copy correct images to temp names (to avoid overwrite during rename)
# New images (upload order): erhu, pipa, guqin, dizi, guzheng, suona
# Mapping by file size comparison:
# erhu correct -> 162224 bytes (upload 1)
# pipa correct -> 155050 bytes (upload 2)
# guqin correct -> 150689 bytes (upload 3)
# dizi correct -> 154649 bytes (upload 4)
# guzheng correct -> 134289 bytes (upload 5)
# suona correct -> 155974 bytes (upload 6)

# Copy correct files to temp names first
correct = {
    'erhu':    'bg-result-guqin.jpg',     # 162224 bytes
    'pipa':    'bg-result-guzheng.jpg',    # 155050 bytes
    'guqin':   'bg-result-dizi.jpg',       # 150689 bytes
    'dizi':    'bg-result-erhu.jpg',        # 154649 bytes
    'guzheng': 'bg-result-pipa.jpg',        # 134289 bytes
    'suona':   'bg-result-suona.jpg',       # 155974 bytes (unchanged)
}

for inst, src_file in correct.items():
    src = path + '\\' + src_file
    dst = path + '\\bg_result_' + inst + '_new.jpg'
    import shutil
    shutil.copy2(src, dst)
    print(f'Copied {src_file} -> bg_result_{inst}_new.jpg ({os.path.getsize(dst)} bytes)')

# Step 2: Rename old files to backup
old_files = ['bg-result-erhu.jpg', 'bg-result-pipa.jpg', 'bg-result-guqin.jpg',
             'bg-result-dizi.jpg', 'bg-result-guzheng.jpg', 'bg-result-suona.jpg']
for f in old_files:
    fpath = path + '\\' + f
    if os.path.exists(fpath):
        os.rename(fpath, fpath + '.bak')
        print(f'Renamed {f} -> {f}.bak')

# Step 3: Rename new files to correct names
for inst in ['erhu', 'pipa', 'guqin', 'dizi', 'guzheng', 'suona']:
    src = path + '\\bg_result_' + inst + '_new.jpg'
    dst = path + '\\bg-result-' + inst + '.jpg'
    os.rename(src, dst)
    print(f'Renamed {os.path.basename(src)} -> bg-result-{inst}.jpg ({os.path.getsize(dst)} bytes)')

print('Done!')
for inst in ['erhu', 'pipa', 'guqin', 'dizi', 'guzheng', 'suona']:
    fpath = path + '\\bg-result-' + inst + '.jpg'
    print(f'  bg-result-{inst}.jpg: {os.path.getsize(fpath)} bytes')
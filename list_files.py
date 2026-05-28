# -*- coding: utf-8 -*-
import os

path = r'C:\Users\32047\lobsterai\project\instrument-personality'
files = os.listdir(path)
for f in sorted(files):
    if 'bg-result' in f or 'result' in f.lower():
        print(f)
print()
for f in sorted(files):
    if f.endswith(('.jpg', '.jpeg', '.png')):
        print(f)
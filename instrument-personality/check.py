import re

with open(r'C:\Users\32047\lobsterai\project\instrument-personality\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_classes = ['token-icon', 'token-knot', 'token-reveal', 'token-name', 'token-tag']
for c in old_classes:
    if c in content:
        print(f'FOUND: {c}')
    else:
        print(f'NOT FOUND: {c}')

print(f'\nFile size: {len(content)} chars')
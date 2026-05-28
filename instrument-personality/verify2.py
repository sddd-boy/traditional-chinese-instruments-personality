# -*- coding: utf-8 -*-
import codecs, re

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    c = f.read()

idx = c.find('function showResult()')
end = c.find('function getDetailTitle')
code = c[idx:end]

sections = re.findall(r'result-section-title[^>]*>([^<]+)', code)
print('Result sections in order:')
for s in sections:
    print(' -', s)

print()
print('compat-grid in showResult:', 'compat-grid' in code)
print('hexagon-chart-wrap in showResult:', 'hexagon-chart-wrap' in code)
print('percent-chart in showResult:', 'percent-chart' in code)
print()
print('File size:', len(c))
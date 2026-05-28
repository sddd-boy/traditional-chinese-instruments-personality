# -*- coding: utf-8 -*-
import codecs

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    c = f.read()

idx = c.find('function showResult()')
end = c.find('function getDetailTitle')
code = c[idx:end]

print('Key function calls in showResult:')
print('getHexChart:', 'getHexChart' in code)
print('getPercentBars:', 'getPercentBars' in code)
print('getCompatSection:', 'getCompatSection' in code)
print('getDetailTitle:', 'getDetailTitle' in code)
print('getDetailContent:', 'getDetailContent' in code)
print()
print('First 50 chars of html construction:')
print(code[:300])
print()
print('Last 200 chars before next function:')
print(code[-200:])
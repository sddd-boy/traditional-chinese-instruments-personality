# -*- coding: utf-8 -*-
import codecs

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    c = f.read()

print('Size:', len(c))
idx = c.find('function getHexChart')
print('getHexChart at:', idx)
if idx >= 0:
    end = c.find('function getPercentBars', idx)
    print('Function body:')
    print(c[idx:end])
    print()
print('hex-label fill:', 'fill:var(--ink-faint)' in c)
print('hex-label CSS found:', '.hex-label{font-family:var(--font-calligraphy);font-size:11px;fill:var(--ink-faint)' in c)
print('stroke-dasharray in code:', 'stroke-dasharray' in c)
print('rgba(80,100,120' in c)
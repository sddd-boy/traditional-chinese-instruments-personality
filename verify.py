# -*- coding: utf-8 -*-
import codecs

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    c = f.read()

print('Size:', len(c))

# Check instrument images
imgs = ['inst-erhu.png', 'inst-pipa.png', 'inst-guqin.png', 'inst-dizi.png', 'inst-guzheng.png', 'inst-suona.png']
for img in imgs:
    status = 'OK' if img in c else 'MISSING'
    print(status, img)

print()
# Check result sections
sections = ['getDetailTitle', 'getHexChart', 'getPercentBars', 'getCompatSection']
for sec in sections:
    status = 'OK' if sec in c else 'MISSING'
    print(status, sec)

print()
# Check the showResult contains new sections
sr = c.find("function showResult()")
sr_end = c.find("function getDetailTitle")
sr_code = c[sr:sr_end]
print('showResult contains:')
print('  getDetailTitle:', 'getDetailTitle' in sr_code)
print('  getHexChart:', 'getHexChart' in sr_code)
print('  getPercentBars:', 'getPercentBars' in sr_code)
print('  getCompatSection:', 'getCompatSection' in sr_code)
print()
print('All checks done')
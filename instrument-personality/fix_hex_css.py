# -*- coding: utf-8 -*-
import codecs

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    c = f.read()

# Add hex-score-label CSS after hex-label
old_css = '.hex-label{font-family:var(--font-calligraphy);font-size:11px;fill:var(--ink-light);letter-spacing:0.05em;text-anchor:middle}'
new_css = '.hex-label{font-family:var(--font-calligraphy);font-size:11px;fill:var(--ink-light);letter-spacing:0.05em;text-anchor:middle}\n.hex-score-label{font-family:var(--font-calligraphy);font-size:10px;fill:var(--ink-faint);text-anchor:middle;opacity:0.7}'

if old_css in c:
    c = c.replace(old_css, new_css)
    print('CSS fixed')
else:
    print('CSS not found - trying partial match')
    idx = c.find('.hex-label{')
    end = c.find('}', idx)
    print('Found at:', idx, '->', repr(c[idx:end+1]))

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(c)
print('Done. Size:', len(c))
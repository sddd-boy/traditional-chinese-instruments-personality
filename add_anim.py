# -*- coding: utf-8 -*-
import codecs

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    c = f.read()

# Add animation-delay to result sections CSS
old_css = '.result-section{margin-bottom:28px;animation:fadeSlideIn 0.6s ease-out forwards}'
new_css = '.result-section{margin-bottom:28px;animation:fadeSlideIn 0.6s ease-out forwards}\n.result-section:nth-child(1){animation-delay:0.1s}\n.result-section:nth-child(2){animation-delay:0.2s}\n.result-section:nth-child(3){animation-delay:0.3s}\n.result-section:nth-child(4){animation-delay:0.4s}\n.result-section:nth-child(5){animation-delay:0.5s}\n.result-section:nth-child(6){animation-delay:0.6s}\n.result-section:nth-child(7){animation-delay:0.7s}'

if old_css in c:
    c = c.replace(old_css, new_css)
    print('Animation CSS added')
else:
    print('Target CSS not found')
    idx = c.find('.result-section{')
    if idx >= 0:
        end = c.find('}', idx)
        print('Found:', repr(c[idx:end+1]))

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(c)
print('Done. Size:', len(c))
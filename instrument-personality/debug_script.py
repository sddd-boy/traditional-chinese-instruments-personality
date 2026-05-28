# -*- coding: utf-8 -*-
import codecs, os

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

# Check the function we need to find
idx = content.find('function getDescription(')
end_script = content.rfind('</script>')
print('getDescription at:', idx, '  script ends at:', end_script)
print('Chars to replace:', end_script - idx)

# Show what the file looks like around that area
print('Around start:', repr(content[idx:idx+80]))
print('Around end:', repr(content[end_script-80:end_script+20]))

print('Total file size:', len(content))
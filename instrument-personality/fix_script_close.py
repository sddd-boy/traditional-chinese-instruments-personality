# -*- coding: utf-8 -*-
import codecs

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

# The closing </script> tag was lost - add it back
if '</script>' not in content:
    content = content + '\n</script>\n</body>\n</html>'
    print('Fixed: added </script></body></html>')
else:
    print('</script> already present')

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(content)

print('Done. Size:', len(content))
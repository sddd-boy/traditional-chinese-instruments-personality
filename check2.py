# Read current file
with open(r'C:\Users\32047\lobsterai\project\instrument-personality\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for old token HTML
if 'token-icon' in content:
    print("Old token-icon class STILL exists in file - update was not applied")
else:
    print("token-icon not found - old structure may be gone")

if 'token-card' in content:
    print("New token-card class EXISTS - update was applied")
else:
    print("token-card not found - update not applied")

# Find the token HTML in current file
import re
tokens = re.findall(r'<div class="token".*?</div>\s*</div>', content[:5000], re.DOTALL)
print(f"\nFound {len(tokens)} token blocks in first 5000 chars")

# Find all div class patterns
all_classes = re.findall(r'class="([^"]*)"', content[:3000])
unique = list(set(all_classes))[:20]
print(f"\nClasses found: {unique}")
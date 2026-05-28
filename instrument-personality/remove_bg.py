# -*- coding: utf-8 -*-
# Remove white background from logo-seal.png
from PIL import Image
import os

src = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal.png'
dst = r'C:\Users\32047\lobsterai\project\instrument-personality\logo-seal-nobg.png'

img = Image.open(src).convert('RGBA')
w, h = img.size
print(f'Image size: {w}x{h}')

# Get corner pixel colors to detect background
corners = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]
print('Corner colors:')
for cx, cy in corners:
    print(f'  ({cx},{cy}): {img.getpixel((cx, cy))}')

# Sample center
print(f'Center: {img.getpixel((w//2, h//2))}')

# Check if PIL/Numpy available
try:
    import numpy as np
    arr = np.array(img)
    print(f'Array shape: {arr.shape}')
    
    # Detect background color from corners
    bg_sample = arr[5, 5]  # near corner
    print(f'BG sample (5,5): {bg_sample}')
    
    # Threshold: treat pixel as background if close to white
    mask = np.all(arr[:, :, :3] > 200, axis=2)  # R,G,B all > 200 = white-ish
    # Also check alpha channel
    if arr.shape[2] == 4:
        alpha_mask = arr[:, :, 3] < 10
        mask = mask | alpha_mask
    
    print(f'White pixels: {np.sum(mask)} / {mask.size}')
    
    # Make white pixels transparent
    arr[:, :, 3] = np.where(mask, 0, arr[:, :, 3])
    
    result = Image.fromarray(arr, 'RGBA')
    result.save(dst)
    print(f'Saved: {dst}')
    
except ImportError:
    print('Numpy not available, trying PIL only')
    # PIL-only approach
    bg_color = img.getpixel((5, 5))[:3]
    print(f'BG color: {bg_color}')
    
    # Simple flood fill or threshold approach
    # For each pixel, if it's close to white, make it transparent
    for y in range(h):
        for x in range(w):
            pixel = img.getpixel((x, y))
            if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
                img.putpixel((x, y), (255, 255, 255, 0))
    
    img.save(dst)
    print(f'Saved (PIL only): {dst}')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import os

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'
content = open(filepath, 'r', encoding='utf-8').read()
print('Current file size:', len(content), 'chars')
print('Token front found:', '.token-front' in content)
print('Token back found:', '.token-back' in content)
print('Token flip JS found:', 'token-card' in content)
# -*- coding: utf-8 -*-
import os
import shutil

# Copy the quiz background image from temp attachments to project folder
src = r'C:\Users\32047\AppData\Local\Temp\lobsterai\attachments\image-1779962174173-00mwjt.png'
dst = r'C:\Users\32047\lobsterai\project\instrument-personality\bg-quiz.png'

shutil.copy2(src, dst)
print('Copied quiz bg to project:', os.path.exists(dst))

# Check existing fonts in project
project = r'C:\Users\32047\lobsterai\project\instrument-personality'
files = os.listdir(project)
print('Project files:', files)
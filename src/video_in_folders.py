"""
Put files into folders based on their names.
This is currently used only for videos, named like video_20191023somethings.mp4
"""

import os

cwd = os.getcwd()
file_list = os.listdir(cwd)
for f in file_list:
    if os.path.isfile(cwd + os.path.sep + f):
        name = f.split('_')
        if name[0] != 'video':
            continue
        else:
            date = name[1]
            year = date[0:4]
            month = date[4:6]
            if not os.path.exists(cwd + os.path.sep + year + '-' + month):
                os.mkdir(cwd + os.path.sep + year + '-' + month + os.path.sep)
            os.rename(cwd + os.path.sep + f, cwd + os.path.sep + year + '-' + month + os.path.sep + f)

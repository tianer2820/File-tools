"""
rename all files in the same folder to a series
i.e. from a.jpg, b.jpg, c.jpg, d.jpg to 0001.jpg 0002.jpg 0003.jpg 0004.jpg
useful when scanning files

please make sure there is NOT a folder named 'files' in cwd
"""

import os
import shutil


def get_abs_path(cwd, filename):
    return cwd + os.sep + filename

ans = input("rename all files here?[Y/N]:")
if ans.lower() == 'y':
    pass
else:
    print("stoped")
    exit(0)

cwd = os.getcwd()
all_list = os.listdir(cwd)
target_files = []
for file in all_list:
    abspath = os.path.abspath(file)
    if type(abspath) is bytes:
        abspath = abspath.decode('utf8')
    if os.path.isfile(abspath):
        target_files.append(abspath)

target_files.sort(key=lambda x: x.split('.')[0:-1])
length = len(target_files)

newfolder = cwd + os.sep + 'files'
os.mkdir(newfolder)

for i in range(length):
    if len(target_files[i].split(".")) > 1:
        extension = '.' + target_files[i].split(".")[-1]
    else:
        extension = ''
    name = "{:0>4d}{}".format(i, extension)
    os.rename(target_files[i], newfolder + os.sep + name)

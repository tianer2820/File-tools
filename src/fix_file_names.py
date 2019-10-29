#!/usr/bin/python3

"""
In linux and mac, downloaded file names can be like %12%34%56, this program decode it with utf8
"""

import os

if input("Are you sure? [y/n]").upper() != 'Y':
    exit(0)

cwd = os.getcwd()
ls = os.listdir(cwd)
files_to_rename = []
for name in ls:
    if ('+' in name or '%' in name) and os.path.isfile(cwd + os.path.sep + name):
        files_to_rename.append(name)

for file in files_to_rename:
    i = 0
    single_chars = []
    while i < len(file):
        if file[i] == '%':
            char = file[i+1:i+3]
            single_chars.append(char)
            i += 3
        else:
            single_chars.append(file[i])
            i += 1

    final_name = b''
    for char in single_chars:
        if len(char) > 1:
            b = bytes([int(char, 16)])
            final_name += b
        else:
            final_name += char.encode('utf8')
    final_name = final_name.decode('utf8')
    final_name = final_name.replace('+', ' ')
    if os.path.exists(cwd + os.path.sep + final_name):
        print(final_name + ' already exists!')
        continue
    print('renamed: ' + file + ' -> ' + final_name)
    os.rename(cwd + os.path.sep + file, cwd + os.path.sep + final_name)

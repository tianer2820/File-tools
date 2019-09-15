#!/usr/bin/python3

"""
This helps you to put all files in folders by their last modification time.
This put files in folders like "2019 01" or "2003 09"...
"""

import os
import datetime

if input("Are you sure? [y/n]").upper() != 'Y':
    exit(0)

cwd = os.getcwd()
files = os.listdir(cwd)
sep = os.path.sep

for f in files:
    if os.path.isdir(cwd + sep + f):
        continue
    stat = os.stat(cwd + sep + f)
    dt = datetime.datetime.fromtimestamp(stat.st_mtime)
    folder_name = '{:0>4d} {:0>2d}'.format(dt.year, dt.month)
    if os.path.isdir(cwd + sep + folder_name):
        os.rename(cwd + sep + f, cwd + sep + folder_name + sep + f)
    elif os.path.isfile(cwd + sep + folder_name):
        print('Name conflict: file {} exists'.format(folder_name))
        exit(1)
    else:
        os.mkdir(cwd + sep + folder_name)
        os.rename(cwd + sep + f, cwd + sep + folder_name + sep + f)

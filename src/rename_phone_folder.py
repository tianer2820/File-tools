"""
convert folder file name style.
from 2019 8 5 to 2019-08-05
"""

import os
import re

cwd = os.getcwd()
file_list = os.listdir(cwd)
print(file_list)
for i in file_list:
    if os.path.isdir(cwd + os.path.sep + i):
        for c in i:
            if c not in '1234567890-_ ':
                break
        else:
            result = re.match('([1234567890]{4})[-_ ]([1234567890]+)[-_ ]?([1234567890]+)?', i)
            if result:
                print(result.groups())
                if len(result.group(2)) == 1:
                    new_name = result.group(1) + '-' + '0' + result.group(2)
                else:
                    new_name = result.group(1) + '-' + result.group(2)
                if result.group(3):
                    if len(result.group(3)) == 1:
                        new_name += '-' + '0' + result.group(3)
                    else:
                        new_name += '-' + result.group(3)
                if os.path.exists(cwd + os.path.sep + new_name):
                    print(new_name, 'already exists!')
                else:
                    os.rename(cwd + os.path.sep + i, cwd + os.path.sep + new_name)
                    print('successfully renamed', new_name)

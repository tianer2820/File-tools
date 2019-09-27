import os
from typing import Dict
import argparse

def read_dat_file(file_path: str) -> Dict[(str, str)]:
    with open(file_path) as f:
        ret = {}
        while True:
            line = f.readline()
            if line == '\n':
                continue
            elif line == '':
                break
            line = line.replace('\n', '')
            i = line.find(' ')
            line = (line[0:i], line[i:])
            ret[line[0].lower()] = line[1].strip(' ')
    return ret

# the output text template
text_temp = '''{name}
ID: {id}
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='read the unturned data')
    parser.add_argument('-out')
    args = parser.parse_args()
    print(args)
    if args['out']:
        f = open(args['out'])
    else:
        f = None

    folder_location = 'C:/Program Files (x86)/Steam/steamapps/common/Unturned'
    item_location = folder_location + os.path.sep + 'Bundles/Items/'
    genre_list = os.listdir(item_location)

    for genre in genre_list:
        print('######### {} #########\n'.format(genre.upper()))
        if f:
            f.write('######### {} #########\n'.format(genre.upper()))

        genre_location = item_location + genre
        item_list = os.listdir(genre_location)
        for item in item_list:
            item_folder = genre_location + os.sep + item + os.sep
            item_file = item_folder + item + '.dat'
            item_english_file = item_folder + 'English.dat'

            if not os.path.isfile(item_file):
                item_file = item_folder + 'Asset.dat'
                if not os.path.isfile(item_file):
                    continue
            d = read_dat_file(item_file)
            text = text_temp.format(name=item.replace('_', ' '), id=d['id'])

            print(text)
            if f:
                f.write(text + '\n')


import os
from shutil import copyfile


src_path = "screenshots"
dest_path = "dataset"

if not os.path.exists(dest_path):
        os.mkdir(dest_path)

file_list = os.path.join(src_path, 'k.txt')
files = []
with open(file_list) as f:
    for line in f:
        files.append(line)

files = [x.strip() for x in files]



for item in files:
    split_ = item.split(',')
    src = os.path.join(src_path, split_[0])
    dest_folder = os.path.join(dest_path, split_[1])
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    dest = os.path.join(dest_folder, split_[0]+'.png')
    print(dest)
    copyfile(src, dest)

import os

directory = 'screenshots'

for filename in os.listdir(directory):
    if filename not in ['.', '..'] and '.' not in filename:
        new_name = filename+'.png'
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        os.rename(old_file, new_file)
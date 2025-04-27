#Список источников
# 1) https://habr.com/ru/companies/ruvds/articles/325522/
# 2) https://pythonworld.ru/moduli/modul-os.html
# 3) https://docs.python.org/
# 4) https://docs.python.org/3.12/library/os.path.html
# 5) https://pythonworld.ru/moduli/modul-shutil.html


import os
import shutil


input_dir = os.environ['input_dir']
output_dir = os.environ['output_dir']
max_depth = None
max_depth_str = os.environ.get('max_depth', '')
if max_depth_str.isdigit():
    max_depth = int(max_depth_str) 
os.makedirs(output_dir, exist_ok = True)
same_name = {}
for folders, subfolders, files in os.walk(input_dir):
    path_input_dir_to_folders = os.path.relpath(folders, input_dir)
    if path_input_dir_to_folders == '.':
        t = 0
    else:
        t = path_input_dir_to_folders.count(os.sep) + 1
    if max_depth is not None and t > max_depth:
        subfolders.clear()
        continue
    for file_name in files:
        file_path = os.path.join(folders, file_name)
        if file_name not in same_name:
            same_name[file_name] = 0
            name = file_name
        else:
            same_name[file_name] += 1
            root, ext = os.path.splitext(file_name)
            name = root + "_" + str(same_name[file_name]) + ext
        save_path = os.path.join(output_dir, name)    
        shutil.copy(file_path, save_path)
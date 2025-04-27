#Список источников
# 1) https://habr.com/ru/companies/ruvds/articles/325522/
# 2) https://pythonworld.ru/moduli/modul-os.html
# 3) https://docs.python.org/
# 4) https://docs.python.org/3.12/library/os.path.html
# 5) https://pythonworld.ru/moduli/modul-shutil.html


import os
import shutil


input = os.environ['input_dir']
output = os.environ['output_dir']
os.makedirs(output)
same_name = {}
for folders, subfolders, files in os.walk(input):
    for file_name in files:
        file_path = os.path.join(folders, file_name)
        if file_name not in same_name:
            same_name[file_name] = 0
            name = file_name
        else:
            same_name[file_name] += 1
            root, ext = os.path.splitext(file_name)
            name = root + "_" + str(same_name[file_name]) + ext
        save_path = os.path.join(output, name)    
        shutil.copy(file_path, save_path)
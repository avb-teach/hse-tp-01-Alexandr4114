import os
import shutil


input = os.environ['input_dir']
output = os.environ['output_dir']
os.makedirs(output, exist_ok = True)
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
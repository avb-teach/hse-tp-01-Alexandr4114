import os
import shutil


input_dir = os.environ['input_dir']
output_dir = os.environ['output_dir']
max_dep = os.environ.get('max_depth', '')
if max_dep.isdigit():
    max_depth = int(max_dep)
else:
    max_depth = None
dir_counter: dict[str, dict[str, int]] = {}
for folders, subfolders, files in os.walk(input_dir):
    rel = os.path.relpath(folders, input_dir)
    if rel == '.':
        parts = []
    else:
        parts = rel.split(os.sep)
    if max_depth is None:
        dir_ = parts[:]
    else:
        if max_depth == 1:
            dir_ = []
        elif len(parts) <= max_depth - 1:        
            dir_ = parts[:]
        else:
            dir_ = parts[-(max_depth - 1):]
    if  dir_:
        dest_dir = os.path.join(output_dir, *dir_)
    else:
        dest_dir = output_dir 
    os.makedirs(dest_dir, exist_ok = True)
    if dest_dir not in dir_counter:
        dir_counter[dest_dir] = {}
    t = dir_counter[dest_dir]
    for file_name in files:
        file_path = os.path.join(folders, file_name)
        if file_name not in t:
            t[file_name] = 0
            name = file_name
        else:
            t[file_name] += 1
            root, ext = os.path.splitext(file_name)
            name = root + "_" + str(t[file_name]) + ext  
        shutil.copy(file_path, os.path.join(dest_dir, name))       
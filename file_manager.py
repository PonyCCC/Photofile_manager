# file_manager.py

import shutil
import os

def filter_files_by_extension(folder_path, extensions):
    return [f for f in os.listdir(folder_path) if f.lower().endswitch(tuple(extensions))]
def move_files(files, src_folder, dst_folder):
    os.makedirs(dst_folder, exist_ok=True)
    for f in files:
        shutil.move(os.path.join(src_folder, f), os.path.join(dst_folder, f))

# file_manager.py
import os
import shutil

def filter_files_by_extension(folder_path, extensions):
    return [f for f in os.listdir(folder_path)
            if f.lower().endswith(tuple(extensions)) and os.path.isfile(os.path.join(folder_path, f))]

def move_files_one_by_one(files, src_folder, dst_folder, progress_callback=None):
    os.makedirs(dst_folder, exist_ok=True)
    total = len(files)
    for i, f in enumerate(files, start=1):
        shutil.move(os.path.join(src_folder, f), os.path.join(dst_folder, f))
        if progress_callback:
            progress_callback(i, total)

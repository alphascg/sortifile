import os
import shutil
from typing import List, Dict

def get_all_files(target_dir: str) -> List[str]:
    entries = os.listdir(target_dir)
    return [os.path.join(target_dir, e) for e in entries if os.path.isfile(os.path.join(target_dir, e))]

def get_all_files_recursive(target_dir: str) -> List[str]:
    all_files = []
    entries = os.listdir(target_dir)
    for entry in entries:
        full_path = os.path.join(target_dir, entry)
        if os.path.isfile(full_path):
            all_files.append(full_path)
        elif os.path.isdir(full_path):
            all_files.extend(get_all_files(full_path))
    return all_files

def match_filetype(filename: str) -> str:
    _, ext = os.path.splitext(filename)
    return ext.lower()

def get_target_folder(file_ext: str, rules: Dict[str, str], base_dir: str) -> str:
    folder_name = rules.get(file_ext)
    if not folder_name:
        folder_name = 'Others'
    return os.path.join(base_dir, folder_name)

def move_file(src: str, dst_folder: str) -> None:
    os.makedirs(dst_folder, exist_ok=True)
    dst_path = os.path.join(dst_folder, os.path.basename(src))
    shutil.move(src, dst_path)

def sort_directory(target_dir: str, rules: Dict[str, str], dry_run: bool = False, silent: bool = False) -> None:
    files = get_all_files_recursive(target_dir)
    files.sort()

    moved_into_subdirs: dict = {}
    total_moved:int = 0
    for file in files:
        ext = match_filetype(file)
        destination_folder = get_target_folder(ext, rules, target_dir)
        
        if destination_folder not in moved_into_subdirs:
            moved_into_subdirs[destination_folder] = 0

        rel_file = os.path.relpath(file, target_dir)
        rel_dst_folder = os.path.relpath(destination_folder, target_dir)
        
        if dry_run:
            if not silent:
                print(f"[DRY-RUN] {rel_file} → {rel_dst_folder}/")
        else:
            move_file(file, destination_folder)
            moved_into_subdirs[destination_folder] += 1
            total_moved += 1
            if not silent:
                print(f"{rel_file} → {rel_dst_folder}/{os.path.basename(file)}")
    print()
    # Finished moving files, proceeding to printing statistics
    for subdir,moved_files in moved_into_subdirs.items():
        print(f"Moved {moved_files} files to {os.path.relpath(subdir, target_dir)}") 
    print(f"\nMoved a total of {total_moved} Files")
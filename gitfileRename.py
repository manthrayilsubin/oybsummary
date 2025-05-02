import os
import re
import subprocess



def sanitize_filename(filename):
    new_name = filename.replace(" ", "_")
    new_name = re.sub(r'[^A-Za-z0-9._-]', '', new_name)
    new_name = new_name.strip(".")
    reserved = ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'LPT1']
    if new_name.split('.')[0].upper() in reserved:
        new_name = f"_{new_name}"
    return new_name



def rename_files_in_repo(root_dir):
    for root, _, files in os.walk(root_dir):
        for filename in files:
            old_path = os.path.join(root, filename)
            new_filename = sanitize_filename(filename)
            new_path = os.path.join(root, new_filename)
            if old_path != new_path:
                # Use git mv to rename
                os.rename(old_path,new_path)
                #subprocess.run(["git", "mv", old_path, new_path], check=True)
                print(f"Renamed: {old_path} -> {new_path}")



if __name__ == "__main__":

    repo_dir = "."  # Current directory (Git repo root)

    rename_files_in_repo(repo_dir)
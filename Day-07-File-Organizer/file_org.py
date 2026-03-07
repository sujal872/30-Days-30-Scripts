import os
import shutil

root_directory = './'

print(f"\n===== Files in {root_directory} =====\n")

def folder_creator(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
    return folder


for dirpath, dirnames, filenames in os.walk(root_directory):
    for file in filenames:

        file_path = os.path.join(dirpath, file)

        if file.endswith('.txt'):
            folder = folder_creator('TXT_files')
            shutil.move(file_path, folder)

        elif file.endswith('.pdf'):
            folder = folder_creator('PDF_files')
            shutil.move(file_path, folder)

        elif file.endswith('.zip'):
            folder = folder_creator('ZIP_files')
            shutil.move(file_path, folder)

        elif file.endswith('.html'):
            folder = folder_creator('HTML_files')
            shutil.move(file_path, folder)

        elif file.endswith('.cpp'):
            folder = folder_creator('CPP_files')
            shutil.move(file_path, folder)

        else:
            pass
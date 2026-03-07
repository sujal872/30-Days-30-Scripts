import os
import shutil

root_directory = "./"

print("\n===== Smart File Organizer Running =====\n")


def create_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


for dirpath, dirnames, filenames in os.walk(root_directory):

    for file in filenames:

        file_path = os.path.join(dirpath, file)

        # extension detect
        extension = os.path.splitext(file)[1]

        # agar extension nahi hai
        if extension == "":
            folder_name = "NO_EXTENSION"
        else:
            folder_name = extension[1:].upper() + "_FILES"

        create_folder(folder_name)

        destination = os.path.join(folder_name, file)

        shutil.move(file_path, destination)

        print(f"Moved: {file} → {folder_name}")
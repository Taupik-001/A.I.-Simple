# import os

# source_directory = "D:\\Pictures\\Manga Collection\\2.5 Dimensional Seduction\\compressed\\"

# # Get a list of all folder names in the source directory
# folder_names = [folder for folder in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, folder))]

# # Print the list of folder names
# for folder_name in folder_names:
#     print(folder_name)
import os
import re

source_directory = (
    "D:\\Pictures\\Manga Collection\\Eiyuu Kyoushitsu"
)


def rename_folders(source_directory):
    folder_names = [
        folder
        for folder in os.listdir(source_directory)
        if os.path.isdir(os.path.join(source_directory, folder))
    ]
    for folder_name in folder_names:
        new_folder_name = re.sub(r"(\d+)-(\d+)", r"\1.\2", folder_name)
        if new_folder_name != folder_name:
            old_path = os.path.join(source_directory, folder_name)
            new_path = os.path.join(source_directory, new_folder_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {folder_name} -> {new_folder_name}")


rename_folders(source_directory)

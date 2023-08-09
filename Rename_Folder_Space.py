import os

source_directory = "D:\\Pictures\\Manga Collection\\Eiyuu Kyoushitsu"

def rename_folders(directory):
    for folder_name in os.listdir(directory):
        if "-" in folder_name:
            new_name = folder_name.replace("-", " ")
            old_path = os.path.join(directory, folder_name)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f'Renamed "{folder_name}" to "{new_name}"')

rename_folders(source_directory)

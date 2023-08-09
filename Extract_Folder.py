import os

# if __name__ == "__main__":
#     # Specify the source directory to monitor
#     source_directory = "D:\\Pictures\\Manga Collection\\2.5 Dimensional Seduction\\compressed"

#     items = os.listdir(source_directory)
#     sorted_zip_files = sorted(item for item in items if item.endswith('.zip'))

#     print("Sorted ZIP files:")
#     for zip_file in sorted_zip_files:
#         print(zip_file)
import zipfile

if __name__ == "__main__":
    # Specify the source directory to monitor
    source_directory = "D:\\Pictures\\Manga Collection\\Eiyuu Kyoushitsu"
    sorted_folders_directory = "D:\\Pictures\\Manga Collection\\Eiyuu Kyoushitsu"

    items = os.listdir(source_directory)
    sorted_zip_files = sorted(item for item in items if item.endswith('.zip'))

    print("Sorted ZIP files:")
    for zip_file in sorted_zip_files:
        zip_file_path = os.path.join(source_directory, zip_file)

        # Extract the filename without extension
        file_name = os.path.splitext(zip_file)[0]

        # Create a directory using the extracted filename
        folder_path = os.path.join(sorted_folders_directory, file_name)
        os.makedirs(folder_path, exist_ok=True)

        # Extract the contents of the ZIP file into the created folder
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(folder_path)

        print(f"Created folder '{file_name}' and extracted contents from '{zip_file}'")


import os
import shutil
import time
import win32file
import pywintypes


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def move_file_with_rename(source, destination):
    filename, file_extension = os.path.splitext(os.path.basename(destination))
    i = 1
    while os.path.exists(destination):
        destination = os.path.join(
            os.path.dirname(destination), f"{filename}_{i}{file_extension}"
        )
        i += 1

    try:
        shutil.move(source, destination)
    except Exception as e:
        print(f"Failed to move {source} to {destination}: {str(e)}")
    else:
        print(f"Moved: {os.path.basename(source)} from {source} to {destination}")


def is_file_in_use(file_path):
    try:
        file_handle = win32file.CreateFile(
            file_path,
            win32file.GENERIC_READ,
            win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE,
            None,
            win32file.OPEN_EXISTING,
            win32file.FILE_ATTRIBUTE_NORMAL,
            None,
        )
        win32file.CloseHandle(file_handle)
        return False
    except pywintypes.error:
        return True


def categorize_file(file_path, source_directory):
    # Rest of the categorization and moving process remains the same...
    if is_file_in_use(file_path):
        print(
            "The file is still being used (e.g., copied, moved, or loaded). Please wait for the background operation to complete."
        )
        return

    else:
        if file_path.lower().endswith(
            (".jpg", ".png", ".jpeg", ".gif", ".webp", ".ico", ".svg")
        ):
            create_directory_if_not_exists("D:\\Pictures")
            move_file_with_rename(
                file_path, os.path.join("D:\\Pictures", os.path.basename(file_path))
            )
        elif file_path.lower().endswith(
            (".doc", ".docx", ".ppt", ".pptx", ".pdf", ".xls", ".xlsx")
        ):
            create_directory_if_not_exists("D:\\Documents")
            move_file_with_rename(
                file_path,
                os.path.join("D:\\Documents", os.path.basename(file_path)),
            )
        elif file_path.lower().endswith((".mp4", ".mkv", ".avi", ".mov")):
            create_directory_if_not_exists("D:\\Videos")
            move_file_with_rename(
                file_path, os.path.join("D:\\Videos", os.path.basename(file_path))
            )
        elif file_path.lower().endswith((".zip", ".rar", ".7z")):
            create_directory_if_not_exists("D:\\Compressed")
            move_file_with_rename(
                file_path,
                os.path.join("D:\\Compressed", os.path.basename(file_path)),
            )
        elif file_path.lower().endswith(
            (".php", ".html", ".txt", ".css", ".js", ".java", ".py", ".cpp", ".sql")
        ):
            create_directory_if_not_exists("D:\\Code")
            move_file_with_rename(
                file_path, os.path.join("D:\\Code", os.path.basename(file_path))
            )
        elif file_path.lower().endswith((".exe", ".app")):
            create_directory_if_not_exists("D:\\Apps")
            move_file_with_rename(
                file_path, os.path.join("D:\\Apps", os.path.basename(file_path))
            )
        elif file_path.lower().endswith((".mp3", ".wav", ".flac", ".ogg", ".m4a")):
            create_directory_if_not_exists("D:\\Sounds")
            move_file_with_rename(
                file_path, os.path.join("D:\\Sounds", os.path.basename(file_path))
            )
        else:
            create_directory_if_not_exists("D:\\Others")
            move_file_with_rename(
                file_path, os.path.join("D:\\Others", os.path.basename(file_path))
            )


def is_folder_in_use(folder_path):
    try:
        folder_handle = win32file.CreateFile(
            folder_path,
            win32file.GENERIC_READ,
            win32file.FILE_SHARE_READ
            | win32file.FILE_SHARE_WRITE
            | win32file.FILE_SHARE_DELETE,
            None,
            win32file.OPEN_EXISTING,
            win32file.FILE_ATTRIBUTE_DIRECTORY,
            None,
        )
        win32file.CloseHandle(folder_handle)
        return False
    except pywintypes.error:
        return True


def move_folder_to_sorted_directory(folder_path, target_directory):
    if is_folder_in_use(folder_path):
        print(
            "The folder is still being used (e.g., copied, moved, or loaded). Please wait for the background operation to complete."
        )
        return

    else:
        folder_name = os.path.basename(folder_path)
        target_path = os.path.join(target_directory, folder_name)

        # Check if the folder name already exists in the target directory
        while os.path.exists(target_path):
            # If it does, add a suffix to the folder name to make it unique
            folder_name += "_1"
            target_path = os.path.join(target_directory, folder_name)

        # Move the folder to the target directory
        shutil.move(folder_path, target_path)
        print(f"Folder '{os.path.basename(folder_path)}' moved to '{target_path}'.")


if __name__ == "__main__":
    # Specify the source directory to monitor
    source_directory = "D:\\_Sorting-File\\"
    sorted_folders_directory = "D:\\Folder\\"

    while True:
        # Get a list of all items (files and folders) in the source directory
        items = os.listdir(source_directory)

        # Sort the items in ascending order based on their names
        sorted_items = sorted(items)

        if not sorted_items:
            print("No file or folder was found in the specified directory.")
        else:
            # Move the first item in the sorted order and exit the script
            first_item = sorted_items[0]
            item_path = os.path.join(source_directory, first_item)

            if os.path.isdir(item_path):
                move_folder_to_sorted_directory(item_path, sorted_folders_directory)
            else:
                categorize_file(item_path, source_directory)

            print("Script executed successfully. One item moved.")
        time.sleep(2)  # Wait for 5 seconds before the next iteration

import os
import requests
import shutil
import time

url = "https://uip3b-kalimantan.com/buku_tamu/upload/aksi_upload"
folder_path = r"Upload\Images"
target_folder = r"Upload\Images"

while True:
    # Get a list of image files in the folder
    image_files = [
        f
        for f in os.listdir(folder_path)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
    ]

    # Sort the image files in descending order
    image_files.sort(reverse=True)

    if len(image_files) > 0:
        # Take the first image file
        file_name = image_files[0]
        file_path = os.path.join(folder_path, file_name)

        # Extract year and month from the file name
        year = file_name[:4]
        month = file_name[5:7]

        # Create folder path using year and month
        folder_path_year_month = os.path.join(target_folder, year, month)

        # Check if the folder exists, if not, create it
        if not os.path.exists(folder_path_year_month):
            os.makedirs(folder_path_year_month)

        # Move the image to the target folder
        target_path = os.path.join(folder_path_year_month, file_name)
        shutil.move(file_path, target_path)
        print("Image moved to", target_path)

        with open(target_path, "rb") as file:
            files = {"berkas": file}
            response = requests.post(url, files=files)

        if response.status_code == 200:
            print("File upload successful.")
        else:
            print("File upload failed:", response.text)

    else:
        print("No image files found in the folder.")

    # Wait for a few seconds before checking again
    time.sleep(2)
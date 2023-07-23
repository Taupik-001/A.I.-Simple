import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the URL: {url}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    if not image_tags:
        print("No images found on the page.")
        return

    new_folder = 'Manga'
    save_folder = 'Download\\Images\\' + new_folder
    os.makedirs(save_folder, exist_ok=True)

    for img in image_tags:
        img_url = img.get('src')
        if not img_url:
            continue

        img_url = urljoin(url, img_url)
        try:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                img_filename = os.path.join(save_folder, os.path.basename(img_url))
                with open(img_filename, 'wb') as f:
                    f.write(img_response.content)
                print(f"Image downloaded: {img_filename}")
            else:
                print(f"Failed to download image: {img_url}")
        except Exception as e:
            print(f"Error while downloading image {img_url}: {str(e)}")

if __name__ == '__main__':
    url = "https://kiryuu.id/yuusha-ni-zenbu-ubawareta-ore-wa-yuusha-no-hahaoya-to-party-wo-kumimashita-chapter-06/"
    download_images(url)

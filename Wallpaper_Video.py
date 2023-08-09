import os
import ctypes
import ctypes.wintypes as wintypes


def set_video_wallpaper(video_path):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    # Convert the video path to a Unicode string
    video_path = os.path.abspath(video_path)
    video_path = video_path.encode("utf-16le")

    # Set the wallpaper using SystemParametersInfoW function
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, video_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
    )


if __name__ == "__main__":
    # Replace 'video_path' with the path of your video file
    # video_path = "C:\\Users\\taupi\\OneDrive\\Pictures\\Wallpaper\\Kita_Chan.mp4"
    video_path = r"C:\Users\taupi\OneDrive\Pictures\Wallpaper\Kita_Chan.mp4"
    # video_path = "C:/Users/taupi/OneDrive/Pictures/Wallpaper/Kita_Chan.mp4"
    set_video_wallpaper(video_path)

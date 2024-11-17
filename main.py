import yt_dlp as ydl
import os
from config import *

def download_youtube_video(url, resolution="720p", output_dir=dPath, download_playlist=False):
    """
    Download a YouTube video at a specified resolution to a designated folder.

    Parameters:
        url (str): URL of the YouTube video to download.
        resolution (str): Desired video resolution (e.g., "720p"). Defaults to "720p".
        output_dir (str): Directory to save the downloaded video. Defaults to the current directory.
    """
    # Ensure the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # yt-dlp options configuration
    options = {
        'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best',  # Select video and audio formats
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),          # Set output path and file name
        'merge_output_format': 'mp4',                                      # Ensure the output format is mp4 after merging
        'noplaylist': not download_playlist                                # True = Download only the video, not the playlist
    }

    try:
        # Create a YoutubeDL object with the specified options
        with ydl.YoutubeDL(options) as ydl_obj:
            # Start the download process
            ydl_obj.download([url])
        print("Download is completed successfully")
    except Exception as e:
        print(f"An error has occurred: {e}")


def download_youtube_playlist(url, resolution="720p", output_dir=dPath):
    """
    Download a YouTube playlist at a specified resolution to a designated folder.

    Parameters:
        url (str): URL of the YouTube playlist to download.
        resolution (str): Desired video resolution (e.g., "720p"). Defaults to "720p".
        output_dir (str): Directory to save the downloaded video. Defaults to the current directory.
    """
    download_youtube_video(url, resolution, output_dir, download_playlist=True)


if __name__ == '__main__':
    # Dev version to be launched from IDE terminal and take interactive input (unless hard-coded)
    link = ''
    #link = "https://www.youtube.com/w..."  # Uncomment and paste a link here to use hardcoded link

    if not link:
        link = input("Enter the link to download: ")

    #download_youtube_video(link)
    download_youtube_playlist(link)

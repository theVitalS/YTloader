#!/usr/bin/python3
import sys
import os
from pytube import YouTube
from config import dPath

def downloadSingle(link):
    try:
        youtubeObject = YouTube(link, on_progress_callback=progress_function)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        print(f"Downloading {youtubeObject.title}")
        youtubeObject.download(dPath)
        sys.stdout.write('\033[K')
        print("Download is completed successfully")
    except Exception as e:
        print(f"An error has occurred: {e}")


def progress_function(stream, chunk, bytes_remaining):
    print("Downloading... ")

if __name__ == '__main__':

    #Dev version to be launched from IDE terminal and take interactive input
    link = input("Enter the link to download: ")

    downloadSingle(link)

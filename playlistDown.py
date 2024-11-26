from bs4 import BeautifulSoup
import requests
import os
from pytube import YouTube
from pytube import Playlist as PyTubePlaylist

class Playlist:
    def __init__(self, playListUrl):
        self.playListUrl = playListUrl
        self.videos = self.get_playlist_videos()
        self.download_videos()

    def get_playlist_videos(self):
        # Using PyTube's Playlist class to get video URLs from a playlist
        playlist = PyTubePlaylist(self.playListUrl)
        return playlist.video_urls

    def download_videos(self):
        fwrite = open("playlist_detail.txt", "a") # Writing all songs from the Playlist on a text file
        for i, url in enumerate(self.videos):
            try:
                yt = YouTube(url)
                video = yt.streams.get_highest_resolution()
                print(f"Downloading: {yt.title} in {destination}")
                video.download(f"{destination}")
                print(f"Downloaded: {yt.title}")
            except Exception as e:
                print(f"Error downloading video {i+1}: {e}")
        fwrite.close()

if __name__ == "__main__":
    print("        _   _____  _             _____                      _                 _           ")
    print("       | | |  __ \| |           |  __ \                    | |               | |          ")
    print("  _   _| |_| |__) | | __ _ _   _| |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ ")
    print(" | | | | __|  ___/| |/ _` | | | | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
    print(" | |_| | |_| |    | | (_| | |_| | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
    print("  \__, |\__|_|    |_|\__,_|\__, |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ")
    print("   __/ |                    __/ |                                                         ")
    print("  |___/                    |___/                                                      v1.0")
    playlist_url = input('Playlist URL: ')
    destination = input('Destination folder: ')
    Playlist(playlist_url)

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print(f'Downdlonding video: {yt.title}, views: {yt.views}')

yt_vid = yt.streams.get_highest_resolution()

yt_vid.download('<your_folder_for_yt_videos>')

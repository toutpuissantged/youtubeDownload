from pytube import Playlist
from pytube import YouTube

previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        print(liveprogress)


yt = YouTube('https://www.youtube.com/watch?v=4zqKJBxRyuo&ab_channel=SleepEasyRelax-KeithSmith')
yt.register_on_progress_callback(on_progress)
yt.streams.filter(only_audio=True).first().download()
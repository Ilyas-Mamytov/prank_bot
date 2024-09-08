from yt_dlp import YoutubeDL
import os
print(os.getcwd())
if os.path.exists('music'):
    os.chdir('music')
else:
    os.mkdir('music')
    os.chdir('music')
print(os.getcwd())

URLS = ['https://www.youtube.com/watch?v=hwOfNhz5TKY',
        'https://www.youtube.com/watch?v=4nRX7NIrrzs']

with YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': '%(title)s.mp3'}) as ydl:
    ydl.download(URLS)

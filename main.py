from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

print("\t\tYoutube audio dowloader\n")
print("If you want to exit, enter nothing as URL\n")

while True:
    link = input("Enter URL : ")
    if link == '':
        print("Thanks for using")
        break
    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
from pytube import YouTube
import os

# this is where the URL is pasted
yt = YouTube(str(input("Enter the URL of the video that you want to download: \n>>")))

# audio extraction
video = yt.streams.filter(only_audio=True).first()

# change the 'destination' input to your own file name
print("Enter the destination (leave blank for current directory)")
destination = "/Users/Miles/MP3"

# downloading the file
out_file = video.download(output_path=destination)

# save file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# results
print(yt.title + " has been successfully downloaded as a .mp3 file.")
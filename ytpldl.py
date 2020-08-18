import os
from pytube import YouTube
import time
import requests

os.chdir("C:/Users/Public/Downloads/") #sets directory to Public/Downloads folder

folder_name = input("Enter a folder name to download: ")
while os.path.exists(folder_name):                      #checks if folder already exists or not
    dec = input("Folder already exist. Do you wanna continue download in that folder? (y/n)")
    if dec == 'y':
        break
    else:
        folder_name = input("Enter different folder name than " + "\"" + folder_name + "\": ")

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

playlist = []
url = input("Enter the playlist URL of youtube: ")  #Takes url of playlist
num_of_vid = int(input("Enter how many videos to download from the playlist: ")) #how many videos to download
data = requests.get(url)
soup = data.text

link = 0
for i in range(0, num_of_vid):
    link = soup.find('"url":"/watch?v=', link)
    link_of_video = soup[link + 7:link + 27]
    lnk = "https://www.youtube.com" + link_of_video
    playlist.append(lnk)
    link += 66

quality = input("\nEnter the quality you prefer(1080,720,480,360,240,144):")#takes the quality
quality = quality + "p"

if len(os.listdir(folder_name)):
    print("Contents in \"" + folder_name + "\" folder: \n")
    for a in os.listdir(folder_name):              #prints the content names of the existing folder
        print(a)
        time.sleep(.05)
else:
    print("\"" + folder_name + "\"" + "is empty. Starting Action!!!")
print()

print("\nPlease wait it my take a while depending on your situation:\n")

for i in range(0, num_of_vid):
    yt = YouTube(playlist[int(i)])
    videos = yt.streams.filter(file_extension="mp4", res=quality)
    video = videos[0]

    directory_contents = [f.split('.mp4', 1)[0] for f in os.listdir(folder_name) if f.endswith('.mp4')]
    
    if video.title in directory_contents:
        print('!!!Skipping video ' + yt.title + '!!!.\nAs it is already downloaded.'.format(video.default_filename))
        print()
        time.sleep(.009)
        continue

    else:
        print("Downloading video no" + str(i+1) + ': ' + yt.title)
        video.download(folder_name)
        print(yt.title + " - has been downloaded !!!")
        print()
        time.sleep(.01)

print("Opening \"" + os.path.curdir + folder_name + "\" in explorer...")
path = os.path.realpath(folder_name)
os.startfile(path)

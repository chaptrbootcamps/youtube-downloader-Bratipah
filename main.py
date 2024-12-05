#Add your code here. You can break it down into different files/modules and place the main running script here
from pytube import YouTube


print("please enter the url")
url = 'Your URL goes here'
my_video = YouTube(url)

print("*****Video Title*******")
print(my_video.title)

print("*****Thumbnail Image******")
print(my_video.thumbnail_url)

print("*******Download video*******") 
for stream in my_video.streams:
    print(stream)

my_video = my_video.streams.get_highest_resolution()

my_video.download()
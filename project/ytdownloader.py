#Program for youtube video download.
#here we are importing youtube from library pytube.
from pytube import YouTube
#here we are importing link of our video.
link=('https://www.youtube.com/watch?v=-mL3GKPXgdo')
yt= YouTube(link)
#here we are getting the title of the video.
print('Title:',yt.title)
#here we are getting views of the the video.
print('View:',yt.views)
#here we are using this function to get highest resolution. 
yd=yt.streams.get_highest_resolution()
#here we are giving the path for the downloaded video.
yd.download('C:\\Users\\anike')

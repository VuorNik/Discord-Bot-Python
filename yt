import urllib
import re

def yt(phrase):
  html = urllib.request.urlopen('https://www.youtube.com/results?search_query='+phrase)
  video_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())
  return video_ids[0]#print(video_ids)

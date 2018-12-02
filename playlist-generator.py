from bs4 import BeautifulSoup
import re
import urllib.request

from urllib.request import urlopen
import json

### Scraping & Downloading every video in a playlist
###########  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# INSTRUCTIONS:
### 1. Put this file into the destination folder where you want all videos to be downloaded
### 2. Alter playlist_homepage_url to be the playlist url that you want to download
playlist_homepage_url = 'https://chinesepod.com/library/courses/all-way-to-intermediate-1/951'
### 3. Click run. Done





page = urlopen(playlist_homepage_url)
page_content = page.read()
soup = BeautifulSoup(page_content, 'lxml')
divs = soup.findAll("div", {"class": "lesson-media"})
link_list = []
for i in range(len(divs)):
	tester = divs[i]
	for a in tester.select('a[href]'):
		link_list.append(a['href'])

for i in range(len(link_list)):
	url = f"https://chinesepod.com{link_list[i]}"
	video_page = urlopen(url)
	video_page_content = video_page.read()
	video_page_render = BeautifulSoup(video_page_content, 'lxml')
	url_ending = ''.join(re.findall(r'(?<=fast.wistia.com/embed/medias/)[^.]*', str(video_page_render)))
	vid_api = f'https://fast.wistia.com/embed/medias/{url_ending}.json'
	
	with urlopen(vid_api) as r:
		result = json.loads(r.read().decode(r.headers.get_content_charset('utf-8')))

	# find video file in json
	list_of_files = re.findall(r'(?<=https://embed-ssl.wistia.com/deliveries/)[^.]*', str(result))
	my_file = f'https://embed-ssl.wistia.com/deliveries/{list_of_files[7]}.bin'

	urllib.request.urlretrieve(my_file, f'{i+1}.mp4')

	print(f'Downloaded video number {i+1} of {len(link_list)}')

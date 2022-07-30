from bs4 import BeautifulSoup
from pip._vendor import requests
import os
import shutil
import re
from bs4 import BeautifulSoup
import uuid

rnd_str = uuid.uuid4().hex
main_name="download_"+rnd_str
main_folder= main_name+"/"
dir = main_folder

if os.path.exists(dir):
	shutil.rmtree(dir)
os.mkdir(main_folder)


site = 'https://academiadeggteee.wisboo.com/dashboard/course/dsggds/main'
response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
#find all jpg,png,gif
img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]
#print (urls)
for url in urls:
	filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
   #with open( '/home/danesh20016/public_html/ts/'+main_folder+filename.group(1), 'wb') as f:
	print (url)
	with open( '/home/danesh20016/public_html/ts/'+main_folder+filename.group(1), 'wb') as f:
	#with open(main_folder+filename.group(1), 'wb') as f:
		if 'http' not in url:
			# sometimes an image source can be relative
			# if it is provide the base url which also happens
			# to be the site variable atm.
			url = '{}{}'.format(site, url)
		response = requests.get(url)
		f.write(response.content)

 #find all css  
for link in soup.findAll('link', href=True):
	#print ("Found the URL:", link['href'])
	if re.search(".css", link['href']):
	   print (link['href'])
	   with open('/home/danesh20016/public_html/ts/'+main_folder+ filename.group(1), 'wb') as f:
		   # with open(main_folder+filename.group(1), 'wb') as f:
		   if 'http' not in url:
			   # sometimes an image source can be relative
			   # if it is provide the base url which also happens
			   # to be the site variable atm.
			   url = '{}{}'.format(site, link['href'])
		   response = requests.get(url)
		   f.write(response.content)
#find all js
link_js = [sc["src"] for sc in soup.find_all("script",src=True)]
for link in link_js:
	print ("Found the URL:", link)
	with open('/home/danesh20016/public_html/ts/'+main_folder+ filename.group(1), 'wb') as f:
		# with open(main_folder+filename.group(1), 'wb') as f:
		if 'http' not in url:
			# sometimes an image source can be relative
			# if it is provide the base url which also happens
			# to be the site variable atm.
			url = '{}{}'.format(site, link)
		response = requests.get(url)
		f.write(response.content)
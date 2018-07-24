import re
import requests
from bs4 import BeautifulSoup

def get_images(site):

    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    images = []
    for img in img_tags:
        images.append(img.get('src'))

    return images

images = get_images("https://www.google.com")

for i in images:
    print(images)

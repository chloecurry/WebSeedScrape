import requests
from lxml import html
from PIL import Image

# Code to retrieve the photos of seeds from their product page on the West Coast Seeds website. 

file = open("..\data\\SeedURLS.txt", "r")
seed_url = file.read()

seed_url_list = seed_url.split("\n")

for url in seed_url_list:
    page = requests.get(url)
    tree = html.fromstring(page.content)

    name = tree.xpath('//h1[@class="header-font-secondary"]/text()')

    img_url = tree.xpath('//img[@class="featured-image "]/@src')

    if(len(name) == 0 or len(img_url) == 0):
        print(url)
    else:
        img = Image.open(requests.get('https:%s' %img_url[0], stream = True).raw)
        img.save('..\img\%s.png' %name[0])
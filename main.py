from bs4 import BeautifulSoup
import requests
import urllib
from io import BytesIO
import tkinter
from PIL import ImageTk, Image
import re

# getting the site
site = requests.get(
    'https://www.playstation.com/en-au/explore/playstation-plus/this-month-on-ps-plus/').content

# making the beautiful soap object
bsObj = BeautifulSoup(site, 'lxml')

# extracting the titles of the games
header_tags = bsObj.find_all(class_='tier4Header')[:2]
first_game = header_tags[0].text.strip()
secound_game = header_tags[1].text.strip()

# extracting the image wrapper
image_wrapper = bsObj.find_all(class_='image-wrapper')[:2]

# geting the image and putting it into a list
image_tags = []
for i in range(len(image_wrapper)):
    image = image_wrapper[i].find('a').find('img').get("src")
    image_tags.append(image)


root = tkinter.Tk()
root.resizable(0, 0)
root.title('Next month PS Plus games')

# geting the image to use in the gui
images = []
for i in range(2):
    with urllib.request.urlopen("https:" + image_tags[i]) as u:
        raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        images.append(image)

# putting it on the screen
image1 = tkinter.Label(root, image=images[0], width=500)
image1.grid(column=0, row=0, padx=50)

image2 = tkinter.Label(root, image=images[1], width=500)
image2.grid(column=1, row=0, padx=50)

# putting the title on the screen
text1 = tkinter.Label(root, text=first_game, font="cursive")
text1.grid(column=0, row=1, padx=50)

text2 = tkinter.Label(root, text=secound_game, font="cursive")
text2.grid(column=1, row=1, padx=50)

root.mainloop()

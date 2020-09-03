from bs4 import BeautifulSoup
import requests
import urllib
from io import BytesIO
import tkinter
from PIL import ImageTk, Image
from tkinter import ttk


def ps_plus_games_next_month():

    # getting the site
    site = requests.get(
        "https://www.playstation.com/en-au/explore/playstation-plus/this-month-on-ps-plus/"
    ).content

    # making the beautiful soap object
    bsObj = BeautifulSoup(site, "lxml")

    # extracting the titles of the games
    header_tags = bsObj.find_all(class_="tier4Header")[:2]
    first_game = header_tags[0].text.strip()
    secound_game = header_tags[1].text.strip()

    # extracting the image wrapper
    image_wrapper = bsObj.find_all(class_="image-wrapper")[:2]

    # geting the image and putting it into a list
    image_tags = []
    for i in range(len(image_wrapper)):
        image = image_wrapper[i].find("a").find("img").get("src")
        image_tags.append(image)

    root = tkinter.Tk()
    root.resizable(0, 0)
    root.title("Next Month PS Plus games")
    root.iconbitmap("Self Work\Playstation\Playstation.ico")

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


def ps_plus_games_this_month():

    # getting the site
    site = requests.get(
        "https://www.playstation.com/en-au/explore/playstation-plus/this-month-on-ps-plus/"
    ).content

    # making the beautiful soap object
    bsObj = BeautifulSoup(site, "lxml")

    # extracting the titles of the games
    header_tags = bsObj.find_all(class_="tier4Header")[2:4]
    first_game = header_tags[0].text.strip()
    secound_game = header_tags[1].text.strip()

    # extracting the image wrapper
    image_wrapper = bsObj.find_all(class_="image-wrapper")[2:4]

    # geting the image and putting it into a list
    image_tags = []
    for i in range(len(image_wrapper)):
        image = image_wrapper[i].find("img").get("src")
        image_tags.append(image)

    root = tkinter.Tk()
    root.resizable(0, 0)
    root.title("This Month PS Plus games")
    root.iconbitmap("Self Work\Playstation\Playstation.ico")

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


def ps_plus_price():
    # getting the site
    site = requests.get(
        "https://www.playstation.com/en-us/explore/playstation-plus/?smcid=other%252525253Aen-us%252525253Ablank%252525253Aprimary%252525252520nav%252525253Amsg-services%252525253Aps-plus"
    ).content

    # making the beautiful soap object
    bsObj = BeautifulSoup(site, "lxml")

    # getting the images
    image_tags = []
    for i in range(10, 13):
        image_tags.append(
            bsObj.find_all(class_="image-block")[i]
            .find("figure")
            .find("picture")
            .find("source")
            .get("srcset")
        )

    root = tkinter.Tk()
    root.title("This Month PS Plus games")
    root.iconbitmap("Self Work\Playstation\Playstation.ico")
    root.resizable(0, 0)

    # geting the image to use in the gui
    images = []
    for i in range(3):
        with urllib.request.urlopen("https:" + image_tags[i]) as u:
            raw_data = u.read()
            im = Image.open(BytesIO(raw_data))
            image = ImageTk.PhotoImage(im)
            images.append(image)

    # putting the image in the gui
    image1 = tkinter.Label(root, image=images[0], width=400, padx=50, pady=50)
    image1.grid(column=0, row=0)

    image2 = tkinter.Label(root, image=images[1], width=400)
    image2.grid(column=1, row=0)

    image3 = tkinter.Label(root, image=images[2], width=400)
    image3.grid(column=2, row=0)

    root.mainloop()


def free_add_ons():

    titles = []
    images = []

    # getting the first page
    site1 = requests.get(
        "https://store.playstation.com/en-us/grid/STORE-MSF77008-PSPLUSEXCLUSIVES/1?price=0-0"
    ).content

    # making the beautiful soap object
    bsObj1 = BeautifulSoup(site1, "lxml")

    for i in range(len(bsObj1.find_all(class_="grid-cell__title"))):
        titles.append(bsObj1.find_all(class_="grid-cell__title")
                      [i].find("span").text)
    for i in range(len(bsObj1.find_all(class_="grid-cell__title"))):
        images.append(
            bsObj1.find_all(
                class_="product-image__img--main")[i].find("img").get("src")
        )

    # getting the next page
    site2 = requests.get(
        "https://store.playstation.com/en-us/grid/STORE-MSF77008-PSPLUSEXCLUSIVES/2?price=0-0"
    ).content

    # making the beautiful soap object
    bsObj2 = BeautifulSoup(site2, "lxml")

    for i in range(len(bsObj2.find_all(class_="grid-cell__title"))):
        titles.append(bsObj2.find_all(class_="grid-cell__title")
                      [i].find("span").text)
    for i in range(len(bsObj2.find_all(class_="grid-cell__title"))):
        images.append(
            bsObj2.find_all(
                class_="product-image__img--main")[i].find("img").get("src")
        )

    # getting the third page
    site3 = requests.get(
        "https://store.playstation.com/en-us/grid/STORE-MSF77008-PSPLUSEXCLUSIVES/3?price=0-0"
    ).content

    # making the beautiful soap object
    bsObj3 = BeautifulSoup(site2, "lxml")

    for i in range(len(bsObj3.find_all(class_="grid-cell__title"))):
        titles.append(bsObj3.find_all(class_="grid-cell__title")
                      [i].find("span").text)
    for i in range(len(bsObj3.find_all(class_="grid-cell__title"))):
        images.append(
            bsObj3.find_all(
                class_="product-image__img--main")[i].find("img").get("src")
        )

    # putting the titles on the gui
    root = tkinter.Tk()
    # root.iconbitmap("Playstation.ico")
    root.title("Free addons")
    root.geometry("1000x1000")
    root.resizable(0, 0)

    # Creating a scroll bar
    # Create a main frame
    main_frame = tkinter.Frame(root)
    main_frame.pack(fill="both", expand=1)

    # Create a canvas
    my_canvas = tkinter.Canvas(main_frame)
    my_canvas.pack(side="left", fill="both", expand=1)

    # Add a scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(
        main_frame, orient="vertical", command=my_canvas.yview)
    my_scrollbar.pack(side="right", fill="y")

    # Configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind(
        "<Configure>", lambda e: my_canvas.configure(
            scrollregion=my_canvas.bbox("all"))
    )

    # Create another frame in the canvas
    secound_frame = tkinter.Frame(my_canvas)

    # Add the new frame to a window in the canvas
    my_canvas.create_window((0, 0), window=secound_frame, anchor="nw")

    # geting the image to use in the gui
    fixed_images = []
    for i in range(len(images)):
        with urllib.request.urlopen(images[i]) as u:
            raw_data = u.read()
            im = Image.open(BytesIO(raw_data))
            image_obj = ImageTk.PhotoImage(im)
            fixed_images.append(image_obj)

    f = 3
    l = 0
    rows = 0
    columns = 0

    for i in range(18):
        for j in range(l, f):
            image_label = tkinter.Label(secound_frame, image=fixed_images[j]).grid(
                row=rows, column=columns, pady=20
            )
            text_label = tkinter.Label(secound_frame, text=titles[j])
            text_label.grid(
                row=rows, column=columns, sticky='s'
            )

            columns += 1

        columns = 0
        rows += 1
        l = f
        f += 3

    root.mainloop()


free_add_ons()

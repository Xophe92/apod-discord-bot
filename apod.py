import random
import requests
import re



def random_image():

    # Generating a random date in 2019
    month = random.choice(range(1, 12))
    day = random.choice(range(1, 28))
    date_in_four_digits = f"{month:0=2d}{day:0=2d}"
    # getting the corresponding page source
    page_url = f"https://apod.nasa.gov/apod/ap19{date_in_four_digits}.html"
    response = requests.get(page_url)
    source = response.text


    # extracting the image present on the page
    pattern = f'IMG SRC="image/19{month:0=2d}/(.*)"'
    image_name = re.search(pattern, source).group(1) # 2do: secure this line
    img_src = f"https://apod.nasa.gov/apod/image/19{month:0=2d}/{image_name}"


    img_data = requests.get(img_src).content
    with open(image_name, 'wb') as handler:
        handler.write(img_data)

    return image_name, page_url

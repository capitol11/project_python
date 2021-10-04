import time
import urllib.request

import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('c:/webdriver/chromedriver.exe')
base_url = 'https://www.google.de'

driver.get(base_url)
search = driver.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search.click()
search.send_keys('Hund')
search.send_keys(Keys.RETURN)
driver.find_element_by_css_selector('#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a').click()

base_url = driver.current_url
driver.get(base_url)
driver.refresh()


# scroll down til the end
last_point = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_point = driver.execute_script("return document.body.scrollHeight")

    if new_point == last_point:
        break
    last_point = new_point

whole_dog_imgs = driver.find_element_by_class_name('islrc')  # parent node
dog_imgs = whole_dog_imgs.find_elements_by_tag_name('img')  # children node
print(len(dog_imgs))


# create img directory if directory not exists
dir = 'Test/img'
try:
    if not os.path.exists(dir):
        os.mkdir(dir)
except OSError:
    print("failed to create directory.")

def check_format(img_source):
    img_format = ""

    img_source = img_url[:img_url.find(',')]

    if 'jpeg' in img_source:
        img_format = '.jpg'
    elif 'png' in img_source:
        img_format = '.png'
    else:
        pass
    return img_format


num_of_pic = 100
not_saved_idx = [] # save idx when img saving doesn't work (ex. None)

for i in range(1, num_of_pic):
    try:
        dog = driver.find_element_by_css_selector(f'#islrg > div.islrc > div:nth-child({i}) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')
        img_url = str(dog.get_attribute('src'))
        name = str(dog.get_attribute('alt'))

        img_format = check_format(img_url)
        if img_format == ".jpg" or img_format == ".png":
            urllib.request.urlretrieve(str(img_url), dir + f"/Hund_{i}" + img_format)
            driver.implicitly_wait(2)
        else:
            urllib.request.urlretrieve(str(img_url), dir + f"/Hund_{i}" + ".jpg")
            driver.implicitly_wait(2)

    except ValueError:
        not_saved_idx.append(i)
        print(f"{i}: invalid URL - {name}")
        print(f"img url: {img_url}")
print("img saving is done.")
print(not_saved_idx)

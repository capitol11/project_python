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


last_point = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    new_point = driver.execute_script("return document.body.scrollHeight")

    if new_point == last_point:
        break
    last_point = new_point

whole_dog_imgs = driver.find_element_by_class_name('islrc')  # Eltern
dog_imgs = whole_dog_imgs.find_elements_by_tag_name('img')  # Kinder
print(len(dog_imgs))


# create img directory if directory not exists
dir = './img'
try:
    if not os.path.exists(dir):
        os.mkdir(dir)
except OSError:
    print("failed to create directory.")


dog = driver.find_element_by_css_selector('#islrg > div.islrc > div:nth-child(1) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')
img_url = dog.get_attribute('src')
urllib.request.urlretrieve(str(img_url), dir+"/Hund_1")
print("img saving is done.")

#for i in range(len(dog_imgs)):
#    driver.find_element_by_css_selector(f'islrg > div.islrc > div:nth-child({i}) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')

import os
import shutil
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://www.chrisburkard.com/Stills/Adventure"

web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')

print(web_soup.findAll("img"))

driver = webdriver.Chrome('/Users/jingwen/opt/anaconda3/lib/python3.9/site-packages/chromedriver_binary/chromedriver') 
driver.get(url)

iterations = 0 
while iterations < 10:
    html = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    print(len(soup.findAll("img")))
    images = []
    for i in soup.findAll("img"):
        src = i["src"]
        images.append(src)
    print(images)
    current_path = os.getcwd()
    for img in images: 
        try:
            file_name = os.path.basename(img, stream=True)
            img_r = requests.get(img, stream=True)
            new_path = os.path.join(current_path, "images", file_name)
            with open(new_path, "wb") as output_file:
                shutil.copyfileobj(img_r.raw, output_file)
            del img_r
        except:
            pass
    iterations += 1
    time.sleep(5)
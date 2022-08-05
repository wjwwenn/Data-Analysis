import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://www.chrisburkard.com/"

web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')
print(web_soup.findAll("img"))

# <img src = ''/> 

driver = webdriver.Chrome('/Users/jingwen/opt/anaconda3/lib/python3.9/site-packages/chromedriver_binary/chromedriver') 
driver.get(url)

html = driver.execute_script("return document.documentElement.outerHTML;")
sel_soup = BeautifulSoup(html, 'html.parser')
print(len(sel_soup.findAll("img")))

images = []
for i in sel_soup.findAll("img"):
    print(i)
    src = i["src"]
    images.append(src)
    
print(images)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('/Users/jingwen/opt/anaconda3/lib/python3.8/site-packages/chromedriver_binary/chromedriver') 
				
url = 'http://qianxi.baidu.com/#/'
driver.get(url)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

soup.find_all(class_="chart-tip")

text=[]

# -- EITHER
for t in soup.find_all('span'):
    t = t.get_text()
    text.append(t.encode('utf-8'))
    print (t)
    
# --- OR
for span in soup.find_all("span", style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:rgba(233,236,255, 1);"):
    text = span.next_sibling

    if text:
        print(span.text, text.strip())
        

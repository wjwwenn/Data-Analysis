from bs4 import BeautifulSoup
import requests

url = "https://www.courts.com.sg/computing-mobile/tablets"

def getdata(url):
    r = requests.get(url)
    return r.text

def html_code(url):
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # display html code
    return (soup)

soup = html_code(url)

def cus_data(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    cus_list = []
  
    for item in soup.find_all("div", "price-box price-final_price"):
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list 
  
cus_res = cus_data(soup)
print(cus_res)

def cus_rev(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
  
    for item in soup.find_all("div", class_=""):
        data_str = data_str + item.get_text()
  
    result = data_str.split("\n")
    return (result)
  
  
rev_data = cus_rev(soup)
rev_result = []
for i in rev_data:
    if i == "":
        pass
    else:
        rev_result.append(i)
rev_result
# -------------------------- BEAUTIFUL SOUP -------------------------- #
# 3B SCRAPING UNSTRUCTURED DATA WITH BEAUTIFUL SOUP
"""
<h3 class="product name product-item-name" style="height: 129px;">
                                <a class="product-item-link" href="https://www.courts.com.sg/microsoft-surface-go-2-64gb-stv-00007-10-5-in-pentium-gold-4425y4gb-64gb-ssd-win-10-home-s-mode2-ip159714">
                                    MICROSOFT SURFACE GO 2 64GB STV-00007 10.5 IN PENTIUM GOLD 4425Y4GB  64GB SSD WIN 10 HOME S MODE2                                </a>
                            </h3>
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.courts.com.sg/computing-mobile/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

data = soup.find_all("h3", "product name product-item-name")
count = 1
for each in data:
    each_title = each.text
    print(f"{count}. {each_title.strip()}")
    count += 1
    
# follow the div then find the class
price = soup.find_all("div", "price-box price-final_price")
prices = price[0]
for each in price:
    each_price = requests.get(url)
    prices.append(each_price)
print(prices)

# follow the div then find the class
div_data = soup.find_all("div", "price-box price-final_price")
#print(div_data[0])
# <span class="special-price">
#print(div_data[0].find("span", "price-wrapper").text)
count = 1
for each in div_data: # loop through all data
    # Get text from tag
    each_price = each.find("span", "price-wrapper").text
    #each_title = each.text # Get the text information from each title.
    print(f"{count}. {each_price.strip()}")# print out the title one by one
    count += 1
"""
<div class="price-box price-final_price" data-role="priceBox" data-product-id="162632" data-price-box="product-id-162632" style="height: 55px;">
        <span class="special-price">


<span class="price-container price-final_price tax weee">
            <span class="price-label">Special Price</span>
        <span id="product-price-162632" data-price-amount="499" data-price-type="finalPrice" class="price-wrapper "><span class="price">S$499.<span class="fraction">00</span></span></span>
        </span>
    </span>
    <span class="old-price">


<span class="price-container price-final_price tax weee">
            <span class="price-label">Regular Price</span>
        <span id="old-price-162632" data-price-amount="618" data-price-type="oldPrice" class="price-wrapper "><span class="price">S$618.<span class="fraction">00</span></span></span>
        </span>
    </span>
    <span class="price-save-amount">(save 19%)</span>

</div>
"""
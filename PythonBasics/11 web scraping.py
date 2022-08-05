import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
loc = 'Newport Beach, CA'
page = 10

url = base_url + loc + "&start=" + str(page)

yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})

# for biz in businesses:
#    print(biz)
#    for title in biz.findAll('a', {'class':'biz-name'}):
#        print(title.text)
    
file_path = 'yelp-{loc}.txt'.format(loc=loc)

with open(file_path, "a") as textfile:
    businesses = yelp_soup.findAll('div', {'class':'biz-listing-large'})
    
    for biz in businesses:
        title = biz.findAll('a', {'class': 'biz-name'})[0].text
        print(title)
        address = biz.findAll('address')[0]
        print(address)
        print('\n')
        phone = biz.findAll('span', {'class': 'biz-phone'})[0].text
        print(phone)
        page_line = "{title}\n{address}\n{phone}".format(
            title = title,
            address = address,
            phone = phone
            )
        textfile.write(page_line)
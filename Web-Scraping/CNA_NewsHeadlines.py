# -------------------------- BEAUTIFUL SOUP -------------------------- #
# 2A - GETTING NEWS HEADLINES  
from bs4 import BeautifulSoup
url = "http://channelnewsasia.com/"
# Make a GET request to fetch the raw HTML content
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

data = soup.find_all("h3", "h3 h3-- list-object__heading")
print(data[0].text)

# ------------------------------------------------  
for each in data: # loop through all the data
    print("Headline: {}".format(each.text))

# -------------- Better alternative
count = 1
for each in data:
    each_title = each.text
    print(f"{count}. {each_title.strip()}")
    count += 1
    

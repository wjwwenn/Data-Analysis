import requests
from requests_oauthlib import OAuth1

consumer_key = 'NZTJrWhij8kemtAXmfyhyA'
consumer_secret = 'JtcAesDkKuNltcKdwR7NEaUkgm8'
token = 'TCipoxU_lYo55-F3rS10XdN6f-3-KQI'
token_secret = '5gAZ99Arn2x_LI0VM25AWy8H84c'

auth = OAuth1(consumer_key, consumer_secret, token, token_secret)

# url = "https://api.yelp.com/v2/search?term=cream+puffs&location=San+Francisco"

# url = 'http://api.yelp.com/v2/search'

# params = {
#    "term": "food",
#    "location": "Newport Beach"
# }

# r =  requests.get(url, auth=auth, params=params)

# print(r.text)

def do_search(term='Food', location='Newport Beach'):
    base_url = 'https://api.yelp.com/v2/search'
    # term = term.replace("", "+")
    # location = location.replace("", "+")
    # url = "{base_url}?term={term}&location={location}".format(
    #           base_url=base_url
    #           term=term,
    #           location=location)
    params = {
        "term":term,
        "location":location,
    }
    auth = OAuth1(consumer_key, consumer_secret, token, token_secret)
    r = requests.get(base_url, auth=auth, params=params)
    return r.json()

search_1 = do_search()

for i in search_1["businesses"]:
    print(i["name"])
    print(i["phone"])
    print(i.get("website"))
    print(i.get("image_url"))
    print(i["location"]["display_address"])
    print(i["location"]["city"])
    print(i.get("location").get("area"))
    print("\n")
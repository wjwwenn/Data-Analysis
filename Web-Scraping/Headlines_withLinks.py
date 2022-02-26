import requests
from bs4 import BeautifulSoup
import re

query = "russia ukraine"
search = query.replace(' ', '+')
results = 500
url = (f"https://www.google.com/search?q={search}&num={results}")

requests_results = requests.get(url)
soup_link = BeautifulSoup(requests_results.content, "html.parser")
links = soup_link.find_all("a")

for link in links:
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
      title = link.find_all('h3')
      if len(title) > 0:
          # get link 
          # print(link.get('href').split("?q=")[1].split("&sa=U")[0])
          print(title[0].getText())
          titles = title[0].getText()
          print("------")
    
          with open("news_headlines.txt", "w") as file:
             file.write(titles)
             
             
# ----------------------------  WORD CLOUD ----------------------------  
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
import  numpy as np
from PIL import Image
import requests

df = open('/Users/jingwen/Desktop/news_headlines.txt', "r")
file = df.readlines()

comment_words = '' 
stopwords = set(STOPWORDS)

for index, data in enumerate(file):
    data = str(data) 
    tokens = data.split() 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
    comment_words += " ".join(tokens)+" "
    
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words)

plt.figure(figsize = (10, 10), facecolor = 'white', edgecolor='blue') 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
# ---------------------  SENTIMENT ANALYSIS ---------------------------- 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
import  numpy as np
from PIL import Image
import requests

import nltk
import pandas as pd 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = open('/Users/jingwen/Desktop/news_headlines.txt', "r")
file = df.readlines()

positive_reviews = []
negative_reviews = []
neutral_reviews = []

analyzer = SentimentIntensityAnalyzer()
    
for index, data in enumerate(file):
    score = analyzer.polarity_scores(data)
    print(score['compound'])
    if score['compound'] < -0.05:
        negative_reviews.append(data)
    elif score['compound'] > 0.05:
        positive_reviews.append(data)
    else:
        neutral_reviews.append(data)
    print(f"{score['compound']} -> {data}") 
          
print("positive_reviews:", len(positive_reviews))
print("negative_reviews:", len(negative_reviews))
print("neutral_reviews:", len(neutral_reviews))

from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
import  numpy as np
from PIL import Image
import requests

import nltk
import pandas as pd 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = open('/Users/jingwen/desktop/restaurant.txt', "r")
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

comment_words = '' 
stopwords = set(STOPWORDS)

for index, data in enumerate(file):
    data = str(data) 
    tokens = data.split() 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
    comment_words += " ".join(tokens)+" "
    
pic = np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png',stream=True).raw))
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, mask = pic, 
                min_font_size = 10).generate(comment_words)

plt.figure(figsize = (10, 10), facecolor = 'white', edgecolor='blue') 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()
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
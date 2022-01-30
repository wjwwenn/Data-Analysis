
import nltk
import pandas as pd 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
df = pd.read_csv("/Users/jingwen/desktop/news.csv")

analyzer = SentimentIntensityAnalyzer()

df.iloc[0,:]

analyzer.polarity_scores(df.iloc[0, -1]) 


positive_news = []
negative_news = []
neutral_news = []

for index, row in df.iterrows():
    print(index, row['clean_text'])
    score = analyzer.polarity_scores(row['clean_text'])
    print(score['compound'])
    if score['compound'] < -0.5:
        negative_news.append(row['clean_text'])
    elif score['compound'] > 0.5:
        positive_news.append(row['clean_text'])
    else:
        neutral_news.append(row['clean_text'])
    print(f"{score['compound']} -> {row['clean_text']}") 
          

print("positive_news:", len(positive_news))
print("negative_news:", len(negative_news))
print("neutral_news:", len(neutral_news))
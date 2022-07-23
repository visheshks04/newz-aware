from flask import Flask, render_template
from predictor import predict
import json
import requests
import os

def get_news():

    NEWS_API_KEY = os.environ['NEWS_API_KEY']

    url = f'https://newsapi.org/v2/top-headlines?country=us&category=politics&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    with open('sampleNews.json', 'w') as f:
        json.dump(response.json(), f, indent=4)
    return response.json()


    # For testing the app use the code below as sample news to avoid large number of API calls
    # file = open('sampleNews.json', 'r')
    # news = json.load(file)

    # return news



def make_predictions():
    articles = get_news()['articles']
    titles = [article['title'] for article in articles]
    url = [article['url'] for article in articles]
    img = [article['urlToImage'] for article in articles]

    predictions = [predict(title) for title in titles]

    for i,pred in enumerate(predictions):
        if pred == 0:
            predictions[i] = 'Right'

        elif pred == 1:
            predictions[i] = 'Neutral'

        else:
            predictions[i] = 'Left'

    list_of_articles = list(zip(titles, url, img, predictions))

    return list_of_articles



app = Flask(__name__)

@app.route('/')
def index():
    
    list_of_articles = make_predictions()

    return render_template('index.html', articles = list_of_articles)


if __name__ == '__main__':
    app.run()
from flask import Flask, render_template
#from predictor import predict
import json
import requests

def get_news():

    # url = 'https://newsapi.org/v2/everything?q=Apple&from=2022-02-08&sortBy=popularity&apiKey=53bb664d5f8e49cebd74327d23c89608'
    # response = requests.get(url)
    # return response.json()

    file = open('sampleNews.json', 'r')
    news = json.load(file)

    return news


app = Flask(__name__)

@app.route('/')
def index():
    articles = get_news()['articles']
    titles = [article['title'] for article in articles]
    url = [article['url'] for article in articles]
    img = [article['urlToImage'] for article in articles]

    # predictions = [predict(title) for title in titles]
    predictions = [0]*len(articles)

    list_of_articles = list(zip(titles, url, img, predictions))
    
    return render_template('index.html', articles = list_of_articles)


if __name__ == '__main__':
    app.run(debug=True)
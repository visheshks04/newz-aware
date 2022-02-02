import pandas as pd
import requests
from bs4 import BeautifulSoup


def fetch_page(df):
    
    title = []
    body = []
    urls = df['url']

    for url in urls:

        res = requests.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')

            title.append(soup.title.text) 
            body.append(soup.body.text)

        else:
            title.append('NULL')
            body.append('NULL')
        
    df['title'] = title 
    df['body'] = body

    return df
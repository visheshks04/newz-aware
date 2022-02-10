import sys
import torch
from model import Model
from data import PreProcessor
import joblib

text = sys.argv[1]


def predict(text):
    preproc = PreProcessor()
    text = preproc.forward(text)

    vectorizer = joblib.load('tfidf_for_bias.pkl')
    text = vectorizer.transform([text])

    text = torch.Tensor(text.toarray())

    model = Model()
    model = torch.load('bias_model.pt')
    model.eval()

    y_pred = []

    for i, data in enumerate(text):
        y_pred.append(model(data))

    fakeness = f'Fakeness Probability: {y_pred[0].item()*100:0.2f}%'

    return fakeness

if __name__ == '__main__':
    predict(text)
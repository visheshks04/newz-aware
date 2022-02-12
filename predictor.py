import torch
from torch.nn import Softmax
from model import Model
from data import PreProcessor
import joblib

def predict(text):
    preproc = PreProcessor()
    text = preproc.forward(text)

    vectorizer = joblib.load('tfidf_for_bias.pkl')
    text = vectorizer.transform([text])
    print(text.shape)
    text = torch.Tensor(text.toarray())
    print(text.shape)
    model = Model()
    model = torch.load('bias_model.pt')
    model.eval()
    print(model.parameters())
    y_pred = []

    for i, data in enumerate(text):
        y_pred.append(model(data))

    fakeness = f'Fakeness Probability: {y_pred[0].item()*100:0.2f}%'

    return fakeness

if __name__ == '__main__':
    text = input()
    prediction = predict(text)
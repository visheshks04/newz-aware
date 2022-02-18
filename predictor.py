from data import PreProcessor
import joblib

def predict(text):
    preproc = PreProcessor()
    text = preproc.forward(text)

    vectorizer = joblib.load('tfidf_for_bias.pkl')
    text = vectorizer.transform([text])

    classifier = joblib.load('naiveBayesModel.pkl')
    pred = classifier.predict(text)

    return pred[0]

if __name__ == '__main__':
    text = input()
    prediction = predict(text)
    print(prediction)
# newz-aware

The growing problem in today's media is that almost every media outlet has some side of political bias to it. There is hardly any media website/channel that is 'neutral' in the true sense. Each one of them is split between either Right or Left. And this really creates an issue for the readers who are not, at the first glance, aware of the biases. This not only causes misunderstanding but also, on its extreme, can cause situations like riots.

Our idea was to help a reader understand and be aware of the kind of bias they are consuming. To do this, we thought of using predictive modeling to detect the bias of media sources. The data that we are using is centric to the political discourse in the USA. It is a crowdsourced dataset that has opinions of both sides (democrats and republicans) on a number of news articles. After building the model. We have a Flask App which fetches the latest news updates from News API (newsapi.org) and displays it along with the bias predicted.

For now, we don't believe it's perfect and we hope to improve and make it better in the future. Possible improvements could be, a more accurate model, a better UI that may also have separate categories for news portals, or different categories for according to the biases.

## Website

Dataset for bias detection: https://deepblue.lib.umich.edu/data/concern/data_sets/8w32r569d?locale=en

There were seven fields in the dataset:

    1) Url
    2) News Type: Has three possible values: other (remember that the articles are sampled from those that are predicted to be political based on our classifiers and so there are false positives we remove based on this label), News, or Opinion.
    3) Perceived (whether the worker was looking at the blinded or unblinded version. perceived=1 means unblinded version)
    4) Primary topic identified by the worker (If "None", the primary topic is not captured by our list of 14 topics)
    5) Secondary topic (If "None", there is no secondary topic or the secondary topic is not captured by our list)
    6) Democratic party  vote
    7) Republican vote

Most of which were not of use to our purpose so we remove all columns except `Url`, `democrat.vote`, `republican.vote`

The votes have 5 possible values `['Negative', 'SomewhatNegative', 'Neutral', 'SomewhatPositive', 'Positive']` which we then label as `[-2,-1,0,1,2]`

Both of the votes are then merged into a single field in the following manner: `bias = democrat.vote - republican.vote`
So a more positive value points to a democrat bias and vice versa.

## Setting up:

    1. We recommend creating a virtual environment using `virtualenv`

    2. Then all the requirements must be installed using `pip3 install -r requirements.txt`

    3.  `train.py` was to train the model.
        `data.py` is the preprocessing pipeline used both in training and predictions.
        `model.py` is the neural network architecture that was built using `nn.Module`
        `predictor.py` is the main program that predicts for new values.
        `test.ipynb` is where most of the data preproc and training was done on Google colab.

    4. You may have to download nltk.corpus.stopwords seperately. Use the following code:
        `import nltk`
        `nltk.download('stopwords')`

    5. You may also have to download en_core_web_sm model seperately. Use the following code:
        `python -m spacy download en_core_web_sm`

## Our Team:

1. Vishesh Kumar Singh (https://github.com/visheshks04)
2. Anuj Jain (https://github.com/anuj1160)
3. Ambuj Kulshreshtha (https://github.com/ambuj-1211)

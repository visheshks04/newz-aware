# newz-aware

Dataset for bias detection: https://deepblue.lib.umich.edu/data/concern/data_sets/8w32r569d?locale=en

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

## Predicting:
    Run the following: `python3 predictor.py 'text-to-be-predicted-comes-here-in-string-quotes-as-an-arg'`


The trained model, state dict and other data can be found here inside this directory: https://drive.google.com/drive/folders/1clx3oHXQzJ9boJB0F_AvCCSecboCkutR?usp=sharing



## Our Team:

1. Vishesh Kumar Singh (https://github.com/visheshks04)
2. Anuj Jain (https://github.com/anuj1160)
3. Ambuj Kulshreshtha (https://github.com/ambuj-1211)

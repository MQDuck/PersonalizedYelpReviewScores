import json

import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
import nltk

np.random.seed(20191211)

nltk.download('wordnet')

stemmer = SnowballStemmer('english')


def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(line):
    text = json.loads(line)
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


# for line in open('data/corpus.json', 'r', encoding='utf8'):
#     review = json.loads(line)
#     print(review)
#     print(preprocess(review))
#     break

corpus = open('data/corpus.json', 'r', encoding='utf8')


import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer

stemmer = SnowballStemmer('english')

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(review):
    result = []
    for token in gensim.utils.simple_preprocess(review):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result
import json
import multiprocessing
import pickle
import time

import gensim
import nltk
import numpy as np
from gensim import models

from parameters import NUM_TOPICS, NO_BELOW, NO_ABOVE
from topic.preprocess import preprocess

if __name__ == '__main__':
    start = time.time()

    np.random.seed(20191211)
    nltk.download('wordnet')

    corpus_file = open('../data/corpus_small.json', 'r', encoding='utf8')
    corpus = [preprocess(json.loads(review)) for review in corpus_file]
    dictionary = gensim.corpora.Dictionary(corpus)
    dictionary.filter_extremes(no_below=NO_BELOW, no_above=NO_ABOVE, keep_n=100000)

    bow_corpus = [dictionary.doc2bow(review) for review in corpus]

    tfidf = models.TfidfModel(bow_corpus)
    corpus_tfidf = tfidf[bow_corpus]

    lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=2,
                                           workers=multiprocessing.cpu_count() // 2 - 1)

    pickle.dump(dictionary, open('dictionary.p', 'wb'))
    pickle.dump(lda_model, open('lda_model.p', 'wb'))

    stop = time.time()
    print(f'total time: {stop - start:.2f} seconds')

    # TEST:
    # unseen_document = 'How a Pentagon deal became an identity crisis for Google'
    # bow_vector = dictionary.doc2bow(preprocess(unseen_document))
    #
    # for index, score in sorted(lda_model[bow_vector], key=lambda tup: -1 * tup[1]):
    #     print("Score: {}\t Topic: {}".format(score, lda_model.print_topic(index, 5)))

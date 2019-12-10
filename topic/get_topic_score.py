import pickle

from topic.preprocess import preprocess

dictionary = pickle.load(open('dictionary.p', 'rb'))
lda_model = pickle.load(open('lda_model.p', 'rb'))

unseen_document = 'How a Pentagon deal became an identity crisis for Google'
bow_vector = dictionary.doc2bow(preprocess(unseen_document))

for index, score in sorted(lda_model[bow_vector], key=lambda tup: -1 * tup[1]):
    print("Score: {}\t Topic: {}".format(score, lda_model.print_topic(index, 5)))

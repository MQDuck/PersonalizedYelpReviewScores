import json

from tqdm import tqdm

businesses = set(json.load(open('data/businesses.json', 'r', encoding='utf8')))
reviews = {}
review_file = open('base_data/review.json', 'r', encoding='utf8')
corpus = []

for line in tqdm(review_file, total=6685900):
    review = json.loads(line)
    business = review['business_id']
    if business in businesses:
        user = review['user_id']
        text = review['text']
        stars = review['stars']
        entry = {'text': text, 'stars': stars}
        if business in reviews:
            reviews[business][user] = entry
        else:
            reviews[business] = {user: entry}

        corpus.append(text)

# json.dump(reviews[len(reviews)//5:], open('data/business_reviews_train.json', 'w', encoding='utf8'))
# json.dump(reviews[:len(reviews)//5], open('data/business_reviews_test.json', 'w', encoding='utf8'))
reviews_items = list(reviews.items())
reviews_train = {k: v for k, v in reviews_items[len(reviews_items) // 5:]}
reviews_test = {k: v for k, v in reviews_items[:len(reviews_items) // 5]}
json.dump(reviews_train, open('data/business_reviews_train.json', 'w', encoding='utf8'))
json.dump(reviews_test, open('data/business_reviews_test.json', 'w', encoding='utf8'))

with open('data/corpus.json', 'w', encoding='utf8') as file:
    for review in corpus:
        line = json.dumps(review) + '\n'
        file.write(line)

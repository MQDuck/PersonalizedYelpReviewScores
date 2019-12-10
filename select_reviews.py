import json

from tqdm import tqdm

businesses = set(json.load(open('data/businesses.json', 'r', encoding='utf8')))
reviews = {}
review_file = open('base_data/review.json', 'r', encoding='utf8')
corpus = []

for line in tqdm(review_file, total=6685900):
    review = json.loads(line)
    business = review['business_id']
    user = review['user_id']
    text = review['text']
    stars = review['stars']
    if business in businesses:
        if business in reviews:
            business_reviews = reviews[business]
        else:
            business_reviews = {}
            reviews[business] = business_reviews
        entry = {'stars': stars, 'text': text}
        if user in business_reviews:
            business_reviews[user].append(entry)
        else:
            business_reviews[user] = [entry]

        corpus.append(text)

json.dump(reviews, open('data/reviews.json', 'w', encoding='utf8'))

with open('data/corpus.json', 'w', encoding='utf8') as file:
    for review in corpus:
        line = json.dumps(review) + '\n'
        file.write(line)

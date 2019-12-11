import json

from tqdm import tqdm

from parameters import NUM_TOPICS
from topic.topic import get_topic_scores

user_weight_sums = {user: {'weight_sums': [0] * NUM_TOPICS, 'n': 0}
                    for user in json.load(open('data/selected_users.json', 'r', encoding='utf8'))}
reviews = json.load(open('data/business_reviews_train.json', 'r', encoding='utf8'))

for business, business_reviews in tqdm(reviews.items()):
    for target_user in user_weight_sums:
        if target_user in business_reviews:
            target_stars = business_reviews[target_user]['stars']
            for user, review in business_reviews.items():
                if user != target_user and abs(review['stars'] - target_stars) < 0.51:
                    topic_scores = get_topic_scores(review['text'])
                    for i, score in topic_scores:
                        user_weight_sums[target_user]['weight_sums'][i] += score
                    user_weight_sums[target_user]['n'] += 1

user_weights = {user: [w / v['n'] for w in v['weight_sums']] for user, v in user_weight_sums.items()}
json.dump(user_weights, open('data/selected_user_weights.json', 'w', encoding='utf8'))

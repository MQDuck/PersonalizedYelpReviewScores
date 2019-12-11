import json

from tqdm import tqdm

from topic.topic import get_topic_scores, get_topic_similarity

user_weights = json.load(open('data/selected_user_weights.json', 'r', encoding='utf8'))
reviews = json.load(open('data/business_reviews_test.json', 'r', encoding='utf8'))

for business, business_reviews in reviews.items():
    for target_user in user_weights:
        if target_user in business_reviews:
            target_stars = business_reviews[target_user]['stars']
            star_sum = 0
            weighted_star_sum = 0
            weight_sum = 0
            num_scores = 0
            for user, review in business_reviews.items():
                if user != target_user:
                    text = review['text']
                    stars = review['stars']
                    # topic_scores = get_topic_scores(text)
                    # weight = 0
                    # for i, score in topic_scores:
                    #     weight += score * user_weights[target_user][i]
                    weight = get_topic_similarity(user_weights[target_user], text)
                    weighted_star_sum += stars * weight
                    weight_sum += weight
                    star_sum += stars
                    num_scores += 1
            predicted_stars = weighted_star_sum / weight_sum
            average = star_sum / num_scores

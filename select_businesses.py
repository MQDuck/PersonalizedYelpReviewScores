import json

from tqdm import tqdm

users = set(json.load(open('data/selected_users.json', 'r', encoding='utf8')))
businesses = set()
user_businesses = {user: set() for user in users}
review_file = open('base_data/review.json', 'r', encoding='utf8')

for line in tqdm(review_file, total=6685900):
    review = json.loads(line)
    user = review['user_id']
    if user in users:
        business = review['business_id']
        businesses.add(business)
        user_businesses[user].add(business)

json.dump(list(businesses), open('data/businesses.json', 'w', encoding='utf8'))
user_businesses = {user: list(businesses) for user, businesses in user_businesses.items()}
json.dump(user_businesses, open('data/selected_users_with_businesses.json', 'w', encoding='utf8'))
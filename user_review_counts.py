import json

from tqdm import tqdm

counts = {}

review_base = open('base_data/review.json', 'r', encoding='utf8')
for line in tqdm(review_base, total=6685900):
    review = json.loads(line)
    user = review['user_id']
    if user in counts:
        counts[user] += 1
    else:
        counts[user] = 1

json.dump(counts, open('data/user_review_counts.json', 'w', encoding='utf8'))

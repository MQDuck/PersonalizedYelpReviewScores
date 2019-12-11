import json
import random

from parameters import NUM_USERS

counts = json.load(open('data/user_review_counts.json', 'r', encoding='utf8'))

sorted_counts = sorted(counts.items(), key=lambda x: -x[1])
selected_users = [user for user, _ in sorted_counts[1000:1000+NUM_USERS]]
random.shuffle(selected_users)

json.dump(selected_users, open('data/selected_users.json', 'w', encoding='utf8'))

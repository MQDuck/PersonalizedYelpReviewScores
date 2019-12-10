import json

from tqdm import tqdm

review_file = open('../base_data/review.json', 'r', encoding='utf8')
corpus_file = open('../data/corpus.json', 'w', encoding='utf8')
for line in tqdm(review_file, total=6685900):
    review = json.loads(line)['text']
    outline = json.dumps(review) + '\n'
    corpus_file.write(outline)

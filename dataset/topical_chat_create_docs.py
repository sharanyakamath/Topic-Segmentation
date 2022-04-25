import pandas as pd
import random
import json

segment_seperator = "========"
MIN_SEGMENTS = 4
MAX_SEGMENTS = 8
DOC_ID = 0
out_dir = f'./data_out_4_8/'
docs_info = {}

# read all sentences from the csv file
data = pd.read_csv('./topical_chat.csv')
docs = []

sentences = [data.iloc[0]['message']]
for i in range(1, len(data)):
    if data.iloc[i]['conversation_id'] != data.iloc[i-1]['conversation_id']:
        docs.append(sentences)
        sentences = []
    sentences.append(data.iloc[i]['message'].strip())

random.shuffle(docs)
i = 0
# create docs with multiple segments
while i < len(docs):
    sentences = []
    t = random.randint(MIN_SEGMENTS, MAX_SEGMENTS)
    for j in range(min(t, len(docs)-i)):
        sentences.append(segment_seperator + ',' + '1' +
                         ',' + str(DOC_ID) + str(j) + '.')
        doc = docs[i+j]
        sentences = sentences + doc
        
    with open(out_dir+str(DOC_ID), 'w', encoding='UTF-8') as out_file:
        out_file.write('\n'.join(sentences))
    
    docs_info[DOC_ID] = len(sentences)-t
    DOC_ID += 1
    i += t

with open(f'4_8.txt', 'w') as file:
     file.write(json.dumps(docs_info))
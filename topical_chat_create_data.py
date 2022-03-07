import pandas as pd
import random
import json

segment_seperator = "========"
SEGMENTS = 3
DOC_ID = 0
out_dir = f'./data_out_{SEGMENTS}/'
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

# create docs with multiple segments
for i in range(0, len(docs), SEGMENTS):
    sentences = []
    
    for j in range(min(SEGMENTS, len(docs)-i)):
        sentences.append(segment_seperator + ',' + '1' +
                         ',' + str(DOC_ID) + str(j) + '.')
        doc = docs[i+j]
        sentences = sentences + doc
        
    with open(out_dir+str(DOC_ID), 'w', encoding='UTF-8') as out_file:
        out_file.write('\n'.join(sentences))
    
    docs_info[DOC_ID] = len(sentences)-SEGMENTS
    DOC_ID += 1

with open(f'{SEGMENTS}.txt', 'w') as file:
     file.write(json.dumps(docs_info))
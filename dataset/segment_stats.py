import pandas as pd
import random
import json
import os
from collections import Counter
from collections import defaultdict
import numpy as np


def get_files(directory):
    files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            files.append(f)
    return files


in_dir = './data_out_5'
files = get_files(in_dir)
total_files = len(files)
print('Total raw files = ', total_files)
print(files[0])
segment_seperator = "========"
sentences = []
segments = []
for cur_file in files:
    with open(cur_file, encoding='UTF-8') as f:
        s_cnt = 0
        cur_words_ar = []
        first_line = True
        for line in f:
            if segment_seperator in line:
                if first_line:
                    first_line = False
                    continue
                segments.append(s_cnt)
                if s_cnt < 100:
                    sentences.extend(cur_words_ar)
                s_cnt = 0
                cur_words_ar = []
                continue
            else:
                s_cnt += 1
                cur_words_ar.append(len(line.split(' ')))
        segments.append(s_cnt)
        if s_cnt < 100:
            sentences.extend(cur_words_ar)

print(len(segments))
segments = list(filter(lambda x: x<100, segments))
print(len(segments))

print("Mean sentence length (no. of words) = ", np.mean(sentences))
print("std sentence length = ", np.std(sentences))

print("Mean segment length (no. of sentences) = ", np.mean(segments))
print("std segment length = ", np.std(segments))
print(len(list(filter(lambda x: x==0, segments))))
import matplotlib.pyplot as plt
plt.plot(np.arange(len(segments)), segments, 'r.') # draws red colored dots
plt.title('Topical Chat')
plt.xlabel('segment number')
plt.ylabel('no of sentences')
plt.ylim([0, 150])
plt.show()
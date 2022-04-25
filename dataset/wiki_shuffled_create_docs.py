import os, sys
import glob
import random

cnt = 0
files = []
segment_seperator = "========"
for filename in glob.iglob("./dev/" + '**/**', recursive=True):
    if 'desktop' not in filename:
        if filename.rstrip('\\').count('\\') >= 4:
            if os.path.isfile(filename):
                cnt += 1
                files.append(filename)
                # print(filename)
print("Total files = ", cnt)
print(files[0])
# stores all the segments in the entire corpus
segments = []
# to store segments per doc
seg_per_doc = []
# k = 0
for file in files:
    with open(file, 'r', encoding='UTF-8') as f:
        cur_seg = ""
        cur_cnt = 0
        for line in f:
            # new segment
            if segment_seperator in line and (",1," in line or ",2," in line):
                if cur_seg != "":
                    cur_seg = cur_seg.rstrip('\n')
                    cur_cnt += 1
                    segments.append(cur_seg)
                cur_seg = line
            else:
                cur_seg += line
        if cur_seg != "":
            cur_seg = cur_seg.rstrip('\n')
            cur_cnt += 1
            segments.append(cur_seg)
        seg_per_doc.append(cur_cnt)
    # k+=1
    # if k > 5:
    #     break
# shuffle segments
random.shuffle(segments)
random.shuffle(seg_per_doc)
k = 0
DOC_ID = 0

# dump segments to file
out_dir = "./shuffled/dev/"
for i in range(len(seg_per_doc)):
    cur_seg_cnt = seg_per_doc[i]
    with open(out_dir+str(DOC_ID), 'w', encoding='UTF-8') as f:
        f.write('\n'.join(segments[k:k+cur_seg_cnt]))
    DOC_ID += 1
    k += cur_seg_cnt

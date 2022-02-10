import xml.etree.ElementTree as ET
import os
import random

out_dir = './data_out/'
in_dir = './data'
DOC_ID = 0
MAX_SEGMENTS = 8
MIN_SEGMENTS = 4
segment_seperator = "========"


def get_files(directory):
    files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            files.append(f)
    return files

files = get_files(in_dir)
total_files = len(files)
print('Total raw files = ', total_files)

# radom shuffle the files order
random.shuffle(files)

i = 0

# create docs
while i < total_files:
	# t is the total segments in current doc
	t = random.randint(MIN_SEGMENTS, MAX_SEGMENTS)
	t = min(t, total_files-i)
	sentences = []
	
	# create a doc with t segments
	# each segment is taken from one source file
	print('cresting doc ', DOC_ID)
	for j in range(t):
		sentences.append(segment_seperator + ',' + '1' + str(DOC_ID) + str(j) + '.')
		f = files[i]
		i+=1
		tree = ET.parse(f)
		root = tree.getroot()
		print(f)
		
		for msg in root[0]:
			# time = msg.attrib['time']
			body = msg[0].text
			if body and len(body) > 0:
				sentences.append(body)
			# print(time, body)
	
	with open(out_dir+str(DOC_ID), 'w', encoding = 'UTF-8') as out_file:
		out_file.write('\n'.join(sentences))
	
	DOC_ID += 1
	i += t

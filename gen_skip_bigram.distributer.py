import sys
from sqlCmd import search_tag

wn = open('skip_bigram_n.txt', 'w')
wv = open('skip_bigram_v.txt', 'w')
wa = open('skip_bigram_a.txt', 'w')
wo = open('skip_bigram_others.txt', 'w')
current_word=''
current_type=0
record=[]
freq=[]
for line in sys.stdin:
	list = line.split('\t')
	words = list[1].split('_')
	if words[0]==current_word:
		record.append(line)
		freq.append(int(list[0]))
	else:
		indexList = sorted(range(len(freq)), key=lambda k: freq[k],  reverse=True)
		for i in range(len(indexList)):
			if current_type==0:
				wn.write(record[indexList[i]])
			elif current_type==1:
				wv.write(record[indexList[i]])
			elif current_type==2:
				wa.write(record[indexList[i]])
			else:
				wo.write(record[indexList[i]])
		record=[]
		freq=[]
		current_word=words[0]
		record.append(line)
		freq.append(int(list[0]))
		tag = search_tag(current_word)
		if tag=='n':
			current_type=0
		elif tag=='v':
			current_type=1
		elif tag=='a':
			current_type=2
		else:
			current_type=3
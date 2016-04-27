from collections import defaultdict
import sys

# cat 2gram_processed.txt | python gen_collocation.py | LC_COLLATE=C sort -t$'\t' -k1 > collocation.2gram.txt

w = open("error.txt","w")
stopwords = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']
for i in range(len(stopwords)):
	stopwords[i] = str(stopwords[i])

for item in stopwords:
	w.write( str(item))
d2_dict = defaultdict(dict)
bigrams=[]
tmp=[]
id=0


f = open("ADJ_final_rank.txt","r")
while True:
	line = f.readline()
	if line=='':
		break
	lists = line.split('\t')
	words = lists[1].split('_')
	if len(words)<2:
		continue
	if d2_dict[words[0]] == {} :
		d2_dict[words[0]]=id
		tmp=[]
		bigrams.append(tmp)
		current_id = id
		id+=1
	else:
		current_id = d2_dict[words[0]]
	bigrams[current_id].append(words[1].replace("\n",""))
f = open("V_final_rank.txt","r")
while True:
	line = f.readline()
	if line=='':
		break
	lists = line.split('\t')
	words = lists[1].split('_')
	if len(words)<2:
		continue
	if d2_dict[words[0]] == {} :
		d2_dict[words[0]]=id
		tmp=[]
		bigrams.append(tmp)
		current_id = id
		id+=1
	else:
		current_id = d2_dict[words[0]]
	bigrams[current_id].append(words[1].replace("\n",""))
f = open("N_final_rank.txt","r")
while True:
	line = f.readline()
	if line=='':
		break
	lists = line.split('\t')
	words = lists[1].split('_')
	if len(words)<2:
		continue
	if d2_dict[words[0]] == {} :
		d2_dict[words[0]]=id
		tmp=[]
		bigrams.append(tmp)
		current_id = id
		id+=1
	else:
		current_id = d2_dict[words[0]]
	bigrams[current_id].append(words[1].replace("\n",""))
	

for i in range(len(bigrams)):
	for j in range(len(bigrams[i])):
		w.write(str(bigrams[i][j]))
	
	
for line in sys.stdin:
	lists = line.split('\t')
	words = lists[0].split(' ')
	try:		
		freq = int(lists[1])
	except IndexError:
		w.write(line)
		continue
	
	has_collocation=0
	if d2_dict[words[0]]!= {} :
		current_id = d2_dict[words[0]]
		for i in range(len(words)):
			if i==0:
				continue
			if words[i] in stopwords:
				if i==len(words)-1 and has_collocation==1:
					print line.replace("\n","")
					break
			if words[i] in bigrams[current_id]:
				has_collocation=1
				if i==len(words)-1 and has_collocation==1:
					print line.replace("\n","")
					break
			else:
				break	
		
		
		
		

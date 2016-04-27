import sys
from sqlCmd import search_lemma

# cat 2.txt | python gen_ngram.map.py | LC_COLLATE=C sort -t$'\t' -k1 | python gen_ngram.reduce.py >2gram.txt
#									 |
#									 v
#							'2gram_processed.txt'

w = open("error.txt","w")

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	if line=="\n": continue
	if line=='': continue
	
	# split the line into words
	list = line.split('\t')
	words = list[0].split(' ')
	try:
		freq = int(list[1])
	except IndexError:
		w.write(line)
		continue
	for i in range(len(words)):
		words[i] = search_lemma(words[i])
	ngram=' '.join(words)
	
	line = line.replace("hasn't","have").replace("doesn't","do").replace("n't","")
	
	print line.replace("\n","")
	
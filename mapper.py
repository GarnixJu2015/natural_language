#!/usr/bin/env python
import sys

# cat skip_bigram_a.txt | python gen_skip_bigram_rank.mapper.py | LC_COLLATE=C sort -t$'\t' -k3 | python gen_skip_bigram_rank.reducer.py | sort -t$'\t' -nrk1 -o'skip_bigram_a_Trank.txt'

# input comes from STDIN (standard input)
rank = 1
preword = None
line = None
for line in sys.stdin:
	# remove leading and trailing whitespace	
	line = line.strip() 	
	if line=="\n": 		
		continue
	
	if line=='': 		
		continue
	# split the line into words
	lists = line.split('\t') #3--> freq val (dist[10])ssss
	freq = int(lists[0])
	words = lists[1].split('_') #value 
	words = words[0]
	#print "word %s preword %s" %(words,preword)
	if words =='':
		continue
	if(words == preword):
		rank= rank + 1
		
	else:
		rank = 1
		preword = words
	print '%d\t%s\t%s\t%s' % (rank,lists[0],lists[1],lists[2])
	
	

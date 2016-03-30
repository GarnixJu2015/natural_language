#!/usr/bin/env python
from collections import defaultdict
import sys
d2_dict = defaultdict(dict)
f = open('Ntable_rank.txt','r')  
lines = f.readlines()
for l in lines:
	# remove leading and trailing whitespace	
	l1 = l.strip() 	
	
	if l1=="\n": 		
		continue
	
	if l1=='': 		
		continue
		
	lists = l1.split('\t')
	rank = lists[0]
	val = lists[2].split('_')
	val = val[1]
	#print val
	d2_dict[val] = int(rank)

for line in sys.stdin:
	# remove leading and trailing whitespace	
	line = line.strip() 	
	if line=="\n": 		
		continue
	
	if line=='': 		
		continue
	# split the line into words
	lists = line.split('\t') #3--> freq val (dist[10])ssss
	rank = int(lists[0])
	val = lists[2].split('_')
	val = val[1]
	if d2_dict[val] != {} :
		value = int(d2_dict[val])
		ans = value/float(rank)	
		if ans > 3 :
			print '%.2f\t%s\t%s' % (ans,lists[2],lists[3])



	

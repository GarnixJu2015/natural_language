import sys
from sqlCmd import search_lemma

#cat ngram.txt | python gen_skip_bigram.mapper.py | LC_COLLATE=C sort -t$'\t' -k1 | python gen_skip_bigram.reducer.py | python gen_skip_bigram.distributer.py

w = open('error.txt', 'w')

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	if line=="\n": continue
	if line=='': continue
	
	# split the line into words
	lists = line.split('\t')
	freq = int(lists[-1])
	dist = int(lists[0])-1
	words = lists[1].split(' ')
	a = search_lemma(words[0])
	b = search_lemma(words[-1])
	if dist>5 or len(a)<1 or len(b)<1:
		w.write(a+'_'+b+'\t'+str(dist)+'\t'+str(freq)+'\n')
	else:
		print '%s_%s\t%d\t%d' % (a,b,dist,freq)
		print '%s_%s\t-%d\t%d' % (b,a,dist,freq)
	'''
	# increase counters
	for i in range(len(words)-1):
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited;
		for k in range(5):
			if i-k>0:
				print '%s_%s\t%d\t%s' % (words[i], words[i-k],(-k),freq)
			if i+k<len(words):
				print '%s_%s\t%d\t%s' % (words[i], words[i+k],k,freq)'''
		
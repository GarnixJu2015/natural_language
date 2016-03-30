import sys

# cat skip_bigram_a.txt | python gen_skip_bigram_rank.mapper.py | LC_COLLATE=C sort -t$'\t' -k1 | python gen_skip_bigram_rank.reducer.py | sort -t$'\t' -nrk1 -o'skip_bigram_a_rank.txt'

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	if line=="\n": continue
	if line=='': continue
	# split the line into words
	lists = line.split('\t')
	freq = int(lists[0])
	words = lists[1].split('_')
	if words[1]=='':
		continue
	text = lists[2]
	#type="N"
	#type="V"
	type="ADJ"
	#type="OTHERS"
	print '%s_%s\t%s\t%d' % (type,words[1],text,freq)
	
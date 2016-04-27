import sys

# cat 2.txt | python gen_ngram.map.py | LC_COLLATE=C sort -t$'\t' -k1 | python gen_ngram.reduce.py >2gram.txt
#									 |
#									 v
#							'2gram_processed.txt'

current_word = None
current_count = 0

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	words = line.split('\t')
	word = words[0]
	count = words[1]

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		continue
	
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
	else:
		if current_word:
			print '%s\t%d' % (current_word, current_count)
		current_count = count
		current_word = word
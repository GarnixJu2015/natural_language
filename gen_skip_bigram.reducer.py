from operator import itemgetter
import sys

current_word = None
current_count = 0
distList = [0,0,0,0,0,0,0,0,0,0,0]
word = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	words = line.split('\t')
	word = words[0]
	if len(word)==1:
		continue
	dist = words[1]
	count = words[2]

	# convert count (currently a string) to int
	try:
		count = int(count)
		dist = int(dist)
	except ValueError:
		continue
	
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
		distList[dist] += count		
	else:
		if current_word:
			print '%d\t%s\t-5(%d) -4(%d) -3(%d) -2(%d) -1(%d) 1(%d) 2(%d) 3(%d) 4(%d) 5(%d)' % ( current_count, current_word, distList[-5], distList[-4],distList[-3],distList[-2],distList[-1],distList[1],distList[2],distList[3],distList[4],distList[5])
		current_count = count
		current_word = word
		distList = [0,0,0,0,0,0,0,0,0,0,0]
		distList[dist] += count

# do not forget to output the last word if needed!
if current_word == word:
	print '%d\t%s\t-5(%d) -4(%d) -3(%d) -2(%d) -1(%d) 1(%d) 2(%d) 3(%d) 4(%d) 5(%d)' % ( current_count, current_word, distList[-5], distList[-4],distList[-3],distList[-2],distList[-1],distList[1],distList[2],distList[3],distList[4],distList[5])
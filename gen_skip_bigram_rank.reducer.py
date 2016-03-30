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
	count = words[-1]
	text = words[-2]
	dist=""
	for i in range(len(text)):
		if text[i]=='(':
			dist+=' '
		elif text[i]!=')':
			dist+=text[i]
	list = dist.split(' ')
			
	# convert count (currently a string) to int
	try:
		count = int(count)
		dist_num=[]
		for i in range(10):
			dist_num.append(int(list[2*(i+1)-1]))
	except ValueError:
		continue
	
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
		for i in range(10):
			distList[i] += dist_num[i]
	else:
		if current_word:
			print '%d\t%s\t-5(%d) -4(%d) -3(%d) -2(%d) -1(%d) 1(%d) 2(%d) 3(%d) 4(%d) 5(%d)' % (current_count, current_word, distList[0], distList[1],distList[2],distList[3],distList[4],distList[5],distList[6],distList[7],distList[8],distList[9])
		current_count = count
		current_word = word
		distList = [0,0,0,0,0,0,0,0,0,0,0]
		for i in range(10):
			distList[i] += dist_num[i]

# do not forget to output the last word if needed!
if current_word == word:
	print '%d\t%s\t-5(%d) -4(%d) -3(%d) -2(%d) -1(%d) 1(%d) 2(%d) 3(%d) 4(%d) 5(%d)' % (current_count, current_word, distList[0], distList[1],distList[2],distList[3],distList[4],distList[5],distList[6],distList[7],distList[8],distList[9])
from operator import itemgetter
import sys

# cat skip_bigram_a.txt | python gen_skip_bigram_rank.mapper.py | LC_COLLATE=C sort -t$'\t' -k1 | python gen_skip_bigram_rank.reducer.py | sort -t$'\t' -nrk1 -o'skip_bigram_a_rank.txt'

# input comes from STDIN (standard input)

prev_freq = 0
current_count = 0
count = 0
word = None
current_word = None
line = None
lists = None 
test = 0
my_array = []
f = open('Ntable_rank.txt', 'w')  
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	if line=="\n": continue
	if line=='': continue
	# split the line into words
	lists = line.split('\t')
	rank = int(lists[0])
	freq = int(lists[1])
	current_word = lists[2].split('_')
	current_word = current_word[0]
	
	strP = str(lists[1])+str('\t')+str(lists[2])+str('\t')+str(lists[3])
	if freq=='':
		continue
	#print 'array %s now %s\n' % (my_array,current_word)
	#print "cur %s now %s\n" % (current_word,word)
	#print 'curword is %s' % current_word

	if current_word != word :		
		if(len(my_array)!=0):
			current_count = current_count//count			
			for obj in my_array:			
				#print '%d\t%s' % (current_count, obj)
				f.write(str(current_count)+"\t"+str(obj)+"\n")
	
		count = 0
		my_array = []
	if count == 0 :
		current_count = 0
		prev_freq = freq

	if(freq == prev_freq):
		current_count = current_count + rank
		count = count + 1
		
		my_array.append(strP)
		word = current_word
		prev_freq = freq
		#print 'rank %d ,current %d, count %d\n' %(rank,current_count, count)
	else:
		#print 'else current %d ,count %d' %(current_count,count)
		current_count = current_count//count
		for obj in my_array:
			test  = test+1 
			#print '%d\t%s' % (current_count, obj)
			f.write(str(current_count)+"\t"+str(obj)+"\n")	
				
		my_array = []
		
		count = 1
		current_count = rank
		my_array.append(strP)
		prev_freq = freq
		word = current_word
		#print 'current %d count %d\n' % (current_count,count)
			

# do not forget to output the last word if needed!
if prev_freq == freq:
	current_count = current_count//count
	for obj in my_array:
			#print '%d\t%s' % (current_count, obj)
			f.write(str(current_count)+"\t"+str(obj)+"\n")
	
	
	

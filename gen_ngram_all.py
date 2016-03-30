w = open('ngram_all.txt', 'w')
for x in range(5):
	x=x+2
	print x
	f = open(str(x)+'.txt', 'r')	#2~6.txt
	while True :
		line = f.readline()
		if line=='':
			f.close()
			break;
		list = line.split('\t')
		words = list[0].split(' ')
		w.write(str(x))
		w.write('\t')
		w.write(str(words[0]))
		w.write(' ')
		w.write(str(words[-1]))
		w.write('\t')
		w.write(list[-1])
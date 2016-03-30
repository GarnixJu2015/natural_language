import re
freq=[]
word=[]
f = open('list_a.txt', 'r')	#f = open('skip_bigram.txt', 'r')
w = open('sorted_list_a.txt', 'w')	#w = open('sorted_skip_bigram.txt', 'w')
while True:
	line = f.readline()
	if line=='': break
	list=line.split('\t')
	word.append(list[0])	#word.append(list[0]+"\t"+list[1])
	freq.append(int(list[1]))	#freq.append(int(list[2]))
indexList = sorted(range(len(freq)), key=lambda k: freq[k],  reverse=True)
for i in range(len(indexList)):
	w.write(word[indexList[i]])	#w.write(str(freq[indexList[i]]))
	w.write("\t")
	w.write(str(freq[indexList[i]]))	#w.write(word[i])
	w.write("\n")
w.close()
f.close()

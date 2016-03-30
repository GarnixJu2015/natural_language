from sqlCmd import search_lemma,search_tag
dict_n={}
dict_v={}
dict_a={}
f = open('1.txt', 'r')
while True :
	line = f.readline()
	list=line.split('\t')
	lemma=search_lemma(list[0])
	tag=search_tag(list[0])
	if(tag=='n'):
		if(lemma not in dict_n):
			dict_n[lemma]=int(list[1])
		else:
			dict_n[lemma]+=int(list[1])
	elif(tag=='v'):
		if(lemma not in dict_v):
			dict_v[lemma]=int(list[1])
		else:
			dict_v[lemma]+=int(list[1])
	elif(tag=='a'):
		if(lemma not in dict_a):
			dict_a[lemma]=int(list[1])
		else:
			dict_a[lemma]+=int(list[1])
		
	if line=='': break
f.close()
f = open('list_n.txt', 'w')
t = dict_n.items()
for i in t:
	if i[0]!="":
		f.write(i[0])
		f.write('\t')
		f.write(str(i[1]))
		f.write('\n')
f = open('list_v.txt', 'w')
t = dict_v.items()
for i in t:
	if i[0]!="":
		f.write(i[0])
		f.write('\t')
		f.write(str(i[1]))
		f.write('\n')
f = open('list_a.txt', 'w')
t = dict_a.items()
for i in t:
	if i[0]!="":
		f.write(i[0])
		f.write('\t')
		f.write(str(i[1]))
		f.write('\n')
import sys

for line in sys.stdin:
	lists = line.split('\t')
	words = lists[0].split(' ')
	if len(words) != 6:
		isPass = 0
	else:
		isPass=1
		for word in words:
			if word == "":
				isPass=0
				break
	if isPass==1:
		print line.replace("\n","")

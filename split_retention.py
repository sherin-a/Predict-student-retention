g = open("datasetHistorical.txt",'r')
lines = g.readlines()
f = open("datasetHistorical_only_retention.txt",'w')
flag = False
lines_to_be_written = []

for line in lines:
	words = line.split("|")
	if words[0] == "g":
		if flag:
			f.write(str("".join(lines_to_be_written)))
		lines_to_be_written = []
		flag = False
		
	if(words[0] == "e"):
		period = int(words[5].replace("\n",""))
		if period > 1:
			flag = True 
	lines_to_be_written.append(line)	
g.close()
f.close()		
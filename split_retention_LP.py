k = open("datasetHistorical_only_retention.txt",'r')
h = open ("historicalLP.txt",'r')
g = open("LPonlyRetention.txt",'w')
lines = h.readlines()
lines_retention = k.readlines()

for line in lines_retention:
	words = line.split("|")
	if(words[0]=="g"):
		Flag = False
		for Lpline in lines:
			LPwords = Lpline.split("|")
			if LPwords[0] == "c":
				if LPwords[1] == words[1]:
					flag = True
				else:
					flag = False
			if flag == True:
				g.write("|".join(LPwords))

g.close()
h.close()
k.close()							
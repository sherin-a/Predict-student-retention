
import BellmanFord
idGraph_idVertice_LabelVertice={}
idGraph_Edge_Weight={}
idGraph_Path={}

def createDatasetLongestPaths(file):
	f = open(file, "r")
	idGraph=None
	for line in f.readlines():
		
		
		if line[0:1].upper()=="G":
	        
			idGraph=line[(line.index('|')+1):-1]
			idGraph_Edge_Weight[idGraph]=[]
			idGraph_Path[idGraph]=[]

		elif line[0:1].upper()=="V":

			lineVertice=line
			fields=lineVertice.split("|")
			idVertice=int(fields[1])
			label=fields[2]
	          			
			idGraph_idVertice_LabelVertice[(idGraph,idVertice)]=label

		elif line[0:1].upper()=="E":

			lineEdge=line
			fields=lineEdge.split("|")
			idSource=fields[1]
			idTarget=fields[3]
			weight=fields[5][:-1]

			edge=fields[1]+","+fields[3]
			idGraph_Edge_Weight[idGraph,edge]=weight
	
	f.close()


if __name__ == '__main__':
	
   
	
	createDatasetLongestPaths("datasetFlowchart.txt")
	f = open("datasetFlowchart.txt",'r')
	lines = f.readlines()
	filename = []
	for line in lines:
		words = line.split("|")
		
		if(words[0]== 'g'):
			fi = words[1].replace("\n","")+".txt"
			filename.append(fi)
			g = open(filename[-1],'w')
			g.write(line)
		else:
			g.write(line)	

	f.close()
	g.close()		
	

	for i in filename:
		#print i
		bf=BellmanFord.Bell()
		idGraph_Path.update(bf.findLongestPathWithBellmanFord(i))
	#print idGraph_Path

	#print idGraph_Edge_Weight

	idGraphs=idGraph_Path.keys()
	datasetPrint=open("flowchartLP.txt","w")
	for idG in idGraphs:
		#map idGraphs to filename

		#for i in filename:
			#name=i.split(".txt")
			#print name[0]
		pathSize=len(idGraph_Path[idG])
		idGraph_LongestPath= "c|"+idG+"|"
		vertice_LongestPath="v|"
		edge_LongestPath="e|"

		

		for t in range(0,pathSize):
			idGraph_LongestPath=idGraph_LongestPath+str(idGraph_Path[idG][t])
			
			if (idGraph_Path[idG][t]!=1):
				idGraph_LongestPath=idGraph_LongestPath+"-"
		datasetPrint.write(idGraph_LongestPath)	
		datasetPrint.write("\n")
	
	
		for t in range(0,pathSize):
			vertice_LongestPath=str(idGraph_Path[idG][t])+"|"+idGraph_idVertice_LabelVertice[(idG,idGraph_Path[idG][t])]
			datasetPrint.write("v|"+vertice_LongestPath)
			datasetPrint.write("\n")

		for t in range(0,pathSize):
			if (t< (pathSize-1)):
					edge=str(idGraph_Path[idG][t])+","+str(idGraph_Path[idG][t+1])
					edge_LongestPath=str(idGraph_Path[idG][t+1])+"|"+idGraph_idVertice_LabelVertice[(idG,idGraph_Path[idG][t+1])]+"|"+str(idGraph_Path[idG][t])+"|"+idGraph_idVertice_LabelVertice[(idG,idGraph_Path[idG][t])]+"|"+str(idGraph_Edge_Weight[(idG,edge)])
					datasetPrint.write("e|"+edge_LongestPath)
					datasetPrint.write("\n")	

								
			
	datasetPrint.close()

			
			

		
		

		

		

	

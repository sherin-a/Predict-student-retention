class Bell:
	marked=None
	topological_order=None
	
	def __init__(self):
		self.marked=[]
		self.topological_order=[]
    	    		
	
	def topologicalOrderWithDFS(self,adjacencyList,v):
		
		self.marked[v]=1
		keys=adjacencyList.keys()

		for i in keys:
			if(i[1]==v):
				        
				if len(adjacencyList[i])!=0:
					for j in adjacencyList[i]:
						if self.marked[j]==0:
							self.topologicalOrderWithDFS(adjacencyList,j)

				self.topological_order.insert(0,v)					
			           		

	def findLongestPathWithBellmanFord(self,file):
		
		f = open(file, "r")
		idGraph=None
		idGraph_Vertices={} 
		idGraph_Edges={} 
		idGraph_idVertice_Neighbors={}
		idGraph_idVertice_Edges={} 
		idGraph_Edge_Weight={} 
		idGraph_idVertice_LabelVertice={} 
		idGraph_Path={}

		lines = f.readlines()
					
		for line in lines:					
		
			if line[0:1]=='g':
		        
				idGraph=line[(line.index('|')+1):-1]
				idGraph_Vertices[idGraph]=[]
				idGraph_Edges[idGraph]=[]
				idGraph_Path[idGraph]=[]

			elif line[0:1].upper()=="V":

				lineVertice=line
				idGraph_Vertices[idGraph].append(lineVertice[:-1])
				fields=lineVertice.split("|")
				idVertice=int(fields[1])
				label=fields[2]
		        
				idGraph_idVertice_Neighbors[(idGraph,idVertice)]=[]
				idGraph_idVertice_Edges[(idGraph,idVertice)]=[]

				idGraph_idVertice_LabelVertice[(idGraph,idVertice)]=label

			elif line[0:1].upper()=="E":

				lineEdge=line
				idGraph_Edges[idGraph].append(lineEdge[:-1])
				fields=lineEdge.split("|")
				idSource=int(fields[1])
				idTarget=int(fields[3])
				weight=float(fields[5])

				idGraph_idVertice_Neighbors[(idGraph,idSource)].append(idTarget)
				edge=fields[1]+","+fields[3]
				idGraph_idVertice_Edges[idGraph,idSource].append(edge)
				weight=weight * -1
				idGraph_Edge_Weight[idGraph,edge]=weight

			
			f.flush()		

				
		idGraphs=idGraph_Edges.keys()
		adjacencyList={}
		
		for idG in idGraphs:
			
			numberOfNodes=len(idGraph_Vertices[idG])

			for i in range(0,numberOfNodes):
				adjacencyList[(idG,i)]=[]


			for w in range(0,numberOfNodes):
				neighbors=idGraph_idVertice_Neighbors[(idG,w)]
				for idNeighbor in neighbors:
					adjacencyList[(idG,w)].append(idNeighbor)		
						
			distance=[]
			precursor=[]
			source=0			
			bf=Bell()

			for i in range(0,numberOfNodes):
				bf.marked.append(0)
						
			bf.topologicalOrderWithDFS(adjacencyList,source);
			length=len(bf.topological_order)

			for i in range(0,numberOfNodes):
				distance.append(float('inf'))
				precursor.append(-1)
			distance[0]=0.0

			for i in range(0,length-1):
				u=bf.topological_order[i]
				
				for j in adjacencyList[(idG,u)]:
					v=j
					edge=str(u)+","+str(v) 
					
					if(distance[v]>(distance[u]+idGraph_Edge_Weight[(idG,edge)])):
						distance[v]=(distance[u]+idGraph_Edge_Weight[(idG,edge)])
						precursor[v]=u
			
			x=1
			while x!=-1:
				idGraph_Path[idG].insert(0,x)
				x=precursor[x]
			
		f.close()	
		return idGraph_Path


		

		


			
	        

			

			



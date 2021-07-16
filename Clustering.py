import sys
import os
import statistics
import networkx as nx
class Clustering:
	def __init__(self):
		pass
	
	def connected_component_subgraphs(self,G):
	    for c in nx.connected_components(G):
	        yield G.subgraph(c)

	def getMCS(self,G_source, G_new):
	    #print(G_source.nodes)
	    #print(G_new.nodes)
	    matching_graph=nx.Graph()

	    for n1,n2 in G_new.edges():
	        if (G_source.has_edge(n1,n2) or G_source.has_edge(n2,n1)):
	            matching_graph.add_node(n1)
	            matching_graph.add_node(n2)
	            matching_graph.add_edge(n1,n2,weight=1)
	    #print(matching_graph.nodes)
	    graphs = list(self.connected_component_subgraphs(matching_graph))
	    #print(len(graphs))
	    mcs_length = 0
	    mcs_graph = nx.Graph()
	    for i, graph in enumerate(graphs):
	        #print(graph.nodes)
	        if len(graph.nodes) > mcs_length:
	            mcs_length = len(graph.nodes)
	            mcs_graph = graph

	    return mcs_graph

	'''
	    creates a networkx digraph from the given file with gspan structure
	'''

	def createGraph(self,sentences):
	    #sentences contains all the lines from the required file
	    DG=nx.DiGraph()
	    
	    for line in sentences:
	        words = line.split("|")
	        if(words[0] == "v"):
	            DG.add_node(str(words[2].replace("\n",'')))
	        if words[0] == "e":    
	            DG.add_node(str(words[2].replace("\n",'')))
	            DG.add_node(str(words[4].replace("\n",'')))
	            DG.add_edge(str(words[2].replace("\n",'')),str(words[4].replace("\n",'')),weight = 1)
	    #print(DG.nodes)
	    return DG    

	def find_distance_3_3(self,lines_curr,lines_stud):
	    #contains the curriculum longest path graph
	    G_source = self.createGraph(lines_curr)
	    #contains the students graph
	    G_new = self.createGraph(lines_stud)
	    #print(G_new.nodes)
	    mcs = self.getMCS(G_source,G_new)
	    mode_mcs = len(mcs.nodes)
	    #print("3.3")
	    #print("MCS:"+str(mode_mcs))
	    
	    #print("Source:"+str(len(G_source)))
	    #print("Dest:"+str(len(G_new.nodes)))
	    if (len(G_new.nodes) == 0):
	        return 0
	    divisor = max (len(G_source.nodes),len(G_new.nodes))
	    #write as float
	    distance = 1 - float(mode_mcs/divisor)  

	    return distance	
	    
	def find_distance_3_4(self,lines_curr,lines_stud):
	    G_source = self.createGraph(lines_curr)
	    #contains the students graph
	    G_new = self.createGraph(lines_stud)
	    #print(G_new.nodes)
	    mcs = self.getMCS(G_source,G_new)
	    mode_mcs = len(mcs.nodes)
	    #print("3.4")
	    #print("MCS:"+str(mode_mcs))
	    
	    #print("Source:"+str(len(G_source)))
	    #print("Dest:"+str(len(G_new.nodes)))

	    divisor = len(G_source.nodes)+len(G_new.nodes)-mode_mcs
	    #print(divisor)
	    #write as float
	    distance = 1 - float(mode_mcs/divisor)  

	    return distance     
	
	def find_distance_3_5(self,lines_curr,lines_stud):
	    G_source = self.createGraph(lines_curr)
	    #contains the students graph
	    G_new = self.createGraph(lines_stud)
	    #print(G_new.nodes)
	    mcs = self.getMCS(G_source,G_new)
	    mode_mcs = len(mcs.nodes)
	 
	    distance = len(G_source.nodes)+len(G_new.nodes)-2*mode_mcs

	    return distance     
	   
import pandas as pd
import numpy as np
import random
#import networkx as nx
from datetime import date

colnames = ['idCurr','idDisc','period_Disc','cht','chp','id_pre_req','period_pre_req']
pre_req=pd.read_csv("C:\\Users\\MALAVIKA P PILLAI\\Downloads\\prerequisites.csv", sep = ';', names=colnames)

f = open("datasetFlowchart.txt", "w")
#G=nx.Graph()
pre_req['period_pre_req'] = np.where(pre_req['period_pre_req'] == "-" , 0 ,pre_req['period_pre_req'] )

idCurriculum = pre_req.idCurr.unique() 

has_pre = pre_req.idDisc.unique()
all_pre = pre_req.id_pre_req.unique()

con = pre_req.id_pre_req.unique()
for i in idCurriculum:
    f.write("g|"+str(i)+"\n")
    fileName = "graph"+str(i).replace(".","")+".gexf"
    #gexfPrint = open(fileName,"w")

    vertices_periods = {'Admission':0}
    vertices_periods ['Conclusion'] = 0
    edges = {}
    new = []
    new2 = []
    """
    gexfPrint.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    gexfPrint.write("<gexf xmlns=\"http://www.gexf.net/1.2draft\" xmlns:viz=\"http://www.gexf.net/1.1draft/viz\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.gexf.net/1.2draft http://www.gexf.net/1.2draft/gexf.xsd\" version=\"1.2\" >\n")
    gexfPrint.write("<meta lastmodifieddate=\""+str(date.today()) +"\">\n")
    gexfPrint.write("<description>Curriculum: " + str(i) + "</description>\n")
    gexfPrint.write("</meta>\n")
    gexfPrint.write("<graph mode=\"static\" defaultedgetype=\"directed\">\n")
    gexfPrint.write("<nodes>\n")
    aux = 9
    """
    for ind in pre_req.index:
		
        if(pre_req['idCurr'][ind] == str(i)):
            vertices_periods [pre_req['id_pre_req'][ind] ] = pre_req['period_pre_req'][ind]
            vertices_periods [pre_req['idDisc'][ind] ] = pre_req['period_Disc'][ind]
            edges [pre_req['idDisc'][ind]] = pre_req['id_pre_req'][ind]
            if pre_req['idDisc'][ind] not in con:
                new.insert(-1,pre_req['idDisc'][ind])
            if pre_req['id_pre_req'][ind] == "-":
                new2.insert(-1,pre_req['idDisc'][ind])    
			
        edges_data = pre_req.loc[pre_req['idCurr'] == i]
	
    x=0
    prevk = "Admission"
   # y = -30
    for key in vertices_periods:
        f.write("v|"+str(x)+"|"+str(key)+"|"+str(vertices_periods[key])+"\n")
        x= x+1
    #    G.add_node(str(key))
    """
        if vertices_periods[prevk] != vertices_periods[key]:
            y = -30
            r = random.randint(0, 255)
            g = random.randint(0, 230)
            b = random.randint(0, 200) 
        
        y = y + aux
        period = str(vertices_periods[key])
        gexfPrint.write("<node id=\"" + str(key) + "\" label=\"" + str(key) + "\">\n")
        gexfPrint.write("<attvalues></attvalues>\n")
        gexfPrint.write("<viz:size value=\"2\"></viz:size>\n")

        sx = period + "9"
        sy = str(y)

        if key == "Admission":
            sx = "-10"
            sy = "-5"
            r = 0
            g = 0
            b = 0
        if key == "Conclusion":
            xOfTheLastVertice = ( len(vertices_periods)* 2) + 30
            sx = str(xOfTheLastVertice)
            sy = "-5"
            r = 0
            g = 0
            b = 0 

        gexfPrint.write("<viz:position x=\"" + sx + "\" y=\"" + sy + "\"></viz:position>\n")
        gexfPrint.write("<viz:color r=\"" + str(r) + "\" g=\"" + str(g) + "\" b=\"" + str(b) + "\"></viz:color>\n")
        gexfPrint.write("</node>\n") 
        
        prevk = key

    gexfPrint.write("</nodes>\n")
    gexfPrint.write("<edges>\n")
    """
    #m = 0
    for key in edges:
        curr_sub = edges_data.loc[edges_data['idDisc'] == key]
        for ind in curr_sub.index:
            f.write("e|"+str(list(vertices_periods).index(curr_sub['id_pre_req'][ind]))+"|"+str(curr_sub['id_pre_req'][ind])+"|"+str(list(vertices_periods).index(key))+"|"+str(key)+"|1\n")
            """ 
            gexfPrint.write("<edge id=\"" + str(m) + "\" source=\"" + str(curr_sub['id_pre_req'][ind]) + "\" target=\"" + str(key) + "\" label=\"" + str(1) + "\">\n")
            gexfPrint.write("<attvalues></attvalues>\n")
            gexfPrint.write("</edge>\n")
            m = m + 1
            """
            #G.add_edge(str(curr_sub['id_pre_req'][ind]),str(key))

    new=np.array(new)
    new = np.unique(new)
    for j in new:
        f.write("e|"+str(list(vertices_periods).index(j))+"|"+str(j)+"|1|Conclusion|1\n")
        """
        gexfPrint.write("<edge id=\"" + str(m) + "\" source=\"" + str(j) + "\" target=\"" + "Conclusion" + "\" label=\"" + str(1) + "\">\n")
        gexfPrint.write("<attvalues></attvalues>\n")
        gexfPrint.write("</edge>\n")
        m = m + 1
        #       G.add_edge(str(j),"Conclusion")
        """
    new2=np.array(new2)
    new2 = np.unique(new2)
    for k in new2:
        f.write("e|0|Admission|"+str(list(vertices_periods).index(k))+"|"+str(k)+"|1\n")
        """
        gexfPrint.write("<edge id=\"" + str(m) + "\" source=\"" + "Admission" + "\" target=\"" + str(k) + "\" label=\"" + str(1) + "\">\n")
        gexfPrint.write("<attvalues></attvalues>\n")
        gexfPrint.write("</edge>\n")
        m = m+ 1
        
        #G.add_edge("Admission",str(k))
        """
    #nx.write_gexf(G, fileName)
    for a in all_pre:
        if a not in has_pre:
            if a in vertices_periods:
                f.write("e|0|Admission|"+str(list(vertices_periods).index(a))+"|"+str(a)+"|1\n")

f.close()
"""
gexfPrint.write("</edges>\n")
gexfPrint.write("</graph>\n")
gexfPrint.write("</gexf>\n")
gexfPrint.close()
"""

import sys
from graphviz import Source
from graphviz import Digraph

filename = str(sys.argv[1])
#filename = input("Enter file name:")
f = open(filename,'r')
edge =[]
vertex =[]
lines = f.readlines()

if filename == "datasetFlowchart.txt":
    course = str(sys.argv[2])
    #course = input("Enter course:")
    #print(course) 
    newfilename = "course"+course.replace(".","")+"dot.gv.txt" 
    
    graphName = course.replace("\n","")
    #print(lines)
    c = ""
    for line in lines:
        words = line.split("|")
        if(words[0] == "g"):
            c=words[1].replace("\n","")
            #print("c is :"+str(c))
            #print(type(course))
            #print(type(c))

            #print(c in course)
        if words[0] == "v" and str(c) == course:
            #print("hi")
            vertex.append(words[2]) 
        if words[0] == "e" and str(c) == course:
            edge.append(line)
else:
    newfilename = filename.replace(".txt","dot.gv.txt")
    for line in lines:
        words = line.split("|")
        if(words[0] == "g"):
           graphName = words[1].replace("\n","")
        if words[0] == "v":
            vertex.append(words[2]) 
        elif words[0] == "e":
            edge.append(line)
f.close()
#print(vertex)
#print(edge)
graphVizPrint = open(newfilename,"w")
graphVizPrint.write("digraph " + graphName.replace(".","") +"\n")
graphVizPrint.write("{\n")
graphVizPrint.write("node[shape=circle fontSize=11]; \n")
for v in vertex:
    graphVizPrint.write(v + " ")
graphVizPrint.write("\n")	
graphVizPrint.write("edge[fontSize=11]\n")

for ed in edge:
    e = ed.split('|')
    graphVizPrint.write("\"" + str(e[2]) + "\"" + " -> \"" + str(e[4]) + "\"[label=\"" + str(e[5].replace("\n","")) + "\"];\n")

graphVizPrint.write("}\n")
graphVizPrint.close()

m = open(newfilename,'r')
lines = m.readlines()

comm = [''.join(lines[:])][0]
#dot =Digraph(body = comm,format = "png")
#print(comm)
src = Source(comm)
src.render(newfilename+'_view.gv', view=True)
#temp = comm	
#dot.render("graph.gv",view = True)
#s = Source(temp, filename="graph.gv", format="png")
#s.view()    
m.close()




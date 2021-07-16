import sys
typeOfGraph = str(sys.argv[1])
sumType = str(sys.argv[2]) # can be sum or nothing
#filename = input("Enter file name:")

g = open("datasetFlowchart.txt",'r')

if sumType == "sum":
    filename = "sumCurr.txt"
else:
    filename = "noCurr.txt"

filewriter = open(filename,"w")

#curriculum_lines = g.readlines()
#take all the curriculums
idCurr = [] # contains all the curriculum ids

curr_edgeWeightsFlowchart = {} #contains curriculum ids and a dict with it which contains the edgeweight of corresponding ids
lines = g.readlines()
edgeWeightsCurr = {}

for line in lines:
    words = line.split("|")
    if(words[0] == "g"):
        idCurr.append(words[1].replace("\n",""))
        curr_edgeWeightsFlowchart[idCurr[-1]] = {}
        

for line in lines:
    words = line.split("|")
    if(words[0] == "g"):
        curr = words[1].replace("\n","")
    if words[0] == "e":
        curr_edgeWeightsFlowchart[curr][str(words[1])+","+str(words[3])] = int(words[5].replace("\n",""))
        

 
    #take vertices too else while creating a file for each curriculum copy till v and only update e   
edgeWeightsStudent = {}
noEdges = {}     

'''
for i in idCurr:
    edgeWeightsStudent [i] = {} #contains the edgeweights of that particular student
    noEdges[i] = {} #contains no of edges for a particular curriculum edge
# by taking key of curr_edgeWeightsFlowchart we can find the edges

'''

if(typeOfGraph == "hist"):
    f = open("datasetHistorical.txt",'r')
    studentLines = f.readlines()
    for line in studentLines:
        words = line.split("|")
        if(words[0].upper() == "G"):
            curr = words[2].replace("\n","")
            #idCurriculumStudent.append(words[2])

        if(words[0].upper() == "E"):
            edgeswithIds = str(words[1])+","+str(words[3])
            
            if sumType == "sum":
                if edgeswithIds not in edgeWeightsStudent[curr]:
                    edgeWeightsStudent[curr][edgeswithIds] = int (words[5].replace("\n","")) + curr_edgeWeightsFlowchart[curr][edgeswithIds]
                else :    
                    edgeWeightsStudent[curr][edgeswithIds] = int (words[5].replace("\n","")) + edgeWeightsStudent[curr][edgeswithIds]
            else:
                if(int (words[5].replace("\n",""))>0):
                    if edgeswithIds not in noEdges[curr]:
                        noEdges[curr][edgeswithIds] = curr_edgeWeightsFlowchart[curr][edgeswithIds] + 1
                    else :
                        noEdges[curr][edgeswithIds] = noEdges[curr][edgeswithIds] + 1   
elif(typeOfGraph == "lp"):
    f = open("datasetPathsHistorical.txt",'r')
    pathLines = f.readlines()
    for line in pathLines:
        words = line.split("|")
        if(words[0].upper() == "C"):
            curr = words[2].replace("\n","")
            #idCurriculumStudent.append(words[2])
        if(words[0].upper() == "E"):
            edgeswithIds = str(words[1])+","+str(words[3])
            
            if sumType == "sum":
                if edgeswithIds not in edgeWeightsStudent[curr]:
                    edgeWeightsStudent[curr][edgeswithIds] = int (words[5].replace("\n","")) + curr_edgeWeightsFlowchart[curr][edgeswithIds]
                else :    
                    edgeWeightsStudent[curr][edgeswithIds] = int (words[5].replace("\n","")) + edgeWeightsStudent[curr][edgeswithIds]
            else:
                if edgeswithIds not in noEdges:
                    noEdges[curr][edgeswithIds] = curr_edgeWeightsFlowchart[curr][edgeswithIds] + 1
                else :
                    noEdges[curr][edgeswithIds] = noEdges[curr][edgeswithIds] + 1  


for line in lines:
    words = line.split("|")
    if(words[0] == "g"):
        filewriter.write(line)
        curr = words[1].replace("\n","")
    if words[0] == "v":
        filewriter.write(line)
    if words[0] == "e":
        edge = str(words[1])+","+str(words[3])
        if sumType == "sum":
            if edge in edgeWeightsStudent[curr]:
                filewriter.write(str(['|'.join(words[:-1])][0])+"|"+str(edgeWeightsStudent[curr][edge])+"\n")
            else:
                filewriter.write(str(['|'.join(words[:-1])][0])+"|"+str(0)+"\n")   
        else:
            if edge in noEdges[curr]:
                filewriter.write(str(['|'.join(words[:-1])][0])+"|"+str(noEdges[curr][edge])+"\n")
            else:
                filewriter.write(str(['|'.join(words[:-1])][0])+"|"+str(0)+"\n")    

f.close()
g.close()
filewriter.close()                
                                         


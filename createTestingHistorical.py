import pandas as pd
import numpy as np
from string import digits
f = open("datasetFlowchart.txt", "r")

h = open("datasetHistorical.txt", "w")

colnames_eq = ['idCurr','idDisc','id_eq']
equivalence=pd.read_csv("equivalences.csv", sep = ';', names=colnames_eq, encoding = "ISO-8859-1" )

colnames_ac = ['idStud','idStatus','Situation','year_sem','idCurr','irrelevant1','irrelevant2']
accompainments=pd.read_csv("accompaniments.csv", sep = ';', names=colnames_ac,encoding = "ISO-8859-1")

colnames_his = ['idStud','year_sem','idDisc','grade','grade_sv','frequency','situation_discipline']
historical=pd.read_csv("historical.csv", sep = ';', names=colnames_his)

idCurr = []
#print(accompainments[1860:])
#print( "219897" in accompainments['idStud'] )
#print(accompainments.loc[accompainments['idStud'] in "145662"])
edges = {}
vertices = {}
edge =[]
vertex =[]

x = 0
#curr = f.readline().split("|")
#idCurr.append(curr[1].replace("\n","")) 
lines = f.readlines()
code = {}

for line in lines:
    words = line.split("|")
    if(words[0] == "g"):
        idCurr.append(words[1].replace("\n",""))
        vertices[idCurr[-1]] = []
        edges[idCurr[-1]] = []
#read from datasetFlowchart.txt

for line in lines:
    words = line.split("|")
    if(words[0] == "g"):
        
        curr = words[1].replace("\n","")
    if words[0] == "v":
        words = line.split("|")
        code[words [2]]=words[1]
        vertices[curr].append(line) 
    elif words[0] == "e":
        edges[curr].append(words)

vertices[idCurr[-1]] = vertex
edges[idCurr[-1]] = edge        

accompainments['idStatus'] = np.where(accompainments['idStatus'] == "\"","",accompainments['idStatus'])
accompainments['idCurr'] = np.where(accompainments['idCurr'] == "\"","",accompainments['idCurr'])

situationDiscNotC = historical[historical["situation_discipline"]!="\"C\""]
#changed next two lines not null to accompainmnts
stud_curr_not_null = accompainments[accompainments.idCurr.notnull()]
studId_graduated = accompainments.idStud.unique()
#stud_graduated = accompainments[accompainments['idStatus'] != "Formado"]
stud_hist = historical.idStud.unique()
#print(stud_hist.shape)
#print(vertices['31.01.001'])


'''
for c in check:
    if c in studId_graduated:
        print(c)
        print(accompainments[accompainments['idStud'] == c].idCurr.mode())
'''        
most_repeat_curr = {}

for stud in studId_graduated:

    stud_curr = stud_curr_not_null[stud_curr_not_null['idStud'] == stud]
    
    most_repeat_curr = stud_curr.idCurr.mode()
    
    his_stud = historical[historical['idStud']==stud]
    s_curr = most_repeat_curr.to_string().replace(" ","").replace("0","",1)
    #print(most_repeat_curr)

    

    if s_curr in vertices :
        fileName = str(stud)+"_"+str(s_curr.replace(" ","").replace(".",""))+".txt"
        #g = open(fileName, "w")
        #g.write("g|"+str(stud)+"|"+str(s_curr.replace(" ","")+"\n"))
        h.write("g|"+str(stud)+"|"+str(s_curr.replace(" ","")+"\n"))

        for v in vertices[s_curr.replace(" ","")]:
            #g.write(v)
            h.write(v)

        stud_eq = {}
        sub = situationDiscNotC[situationDiscNotC["idStud"] == stud].idDisc
        for s in sub:
            if equivalence[equivalence['idDisc'] == s].id_eq.empty == False:
                stud_eq[s] = equivalence[equivalence['idDisc'] == s].id_eq.to_string().replace(" ","").replace("\n","', '")[-7:]

            
        for e in edges[s_curr.replace(" ","")]:

            if(e[2] == "Admission"):
                #g.write(str(['|'.join(e[:])][0]))
                h.write(str(['|'.join(e[:])][0]))
            frequency = his_stud[his_stud['idDisc'] == e[2]].count().idDisc
            
            #counting the repetitions  
            if(frequency != 0):       
                #g.write(str(['|'.join(e[:5])][0]) +"|" + str(frequency)+"\n")
                h.write(str(['|'.join(e[:5])][0]) +"|" + str(frequency)+"\n")
            else:
                #g.write(str(['|'.join(e[:])][0]))
                h.write(str(['|'.join(e[:])][0]))   
            
            #writing equivalence edges
            if e[2] != 'Admission':
                if(e[2] in stud_eq):
                    for x in stud_eq[e[2]]:  
                        weightedge =0  
                        weightedge = his_stud[his_stud['idDisc'] == x].count().idDisc
                        if x in sub:
                            #g.write("e|"+str(code[x])+"|"+str(x)+str(['|'.join(e[3:5])][0])+"|"+str(weightedge)+"\n")
                            h.write()        
                      
        #g.flush()
        #g.close()  
              
h.close()

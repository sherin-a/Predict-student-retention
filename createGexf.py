import random
import pandas as pd
f = open("datasetFlowchart.txt", "r")
lines = f.readlines()


colnames = ['idCurr','idDisc','period_Disc','cht','chp','id_pre_req','period_pre_req']
pre_req=pd.read_csv("C:\\Users\\MALAVIKA P PILLAI\\Downloads\\prerequisites.csv", sep = ';', names=colnames)

idCurr = pre_req.idCurr.unique()

enter = False
x = 0
for i in idCurr:
    print(str(x)+"."+str(i))
    x = x+1
c=input("Enter the choice: ")
ind =0
noOfVertices = 1
fileName = idCurr[int(c)].replace(".","")+".gexf"
gexfPrint = open(fileName,"w")

for line in lines:
    #print(line)
    words = line.split('|')
    #print(words)
    if words[0] == 'g':
        curr = words[1].replace(".","")
        curr = curr.replace("\n","")
    if  curr == idCurr[int(c)].replace(".","") :
        enter = True
    else:
        enter = False
    if words[0] == 'g' and enter == True:
        
        #idCurr.insert(-1,fileName)

        
        gexfPrint.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        gexfPrint.write("<gexf xmlns=\"http://www.gexf.net/1.1draft\" version=\"1.1\" xmlns:viz=\"http://www.gexf.net/1.1draft/viz\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.gexf.net/1.1draft http://www.gexf.net/1.1draft/gexf.xsd\">\n")
        gexfPrint.write("<meta>\n")
        gexfPrint.write("<description>Curriculum: " + words[1] + "</description>\n")
        gexfPrint.write("</meta>\n")
        gexfPrint.write("<graph defaultedgetype=\"directed\" timeformat=\"double\" mode=\"dynamic\">\n")
        gexfPrint.write("<nodes>\n")
        aux = 9
        prev = words [0]
    elif words[0] == "v" and enter == True :
        if prev == "g":
            prevp = words[3]
        y = 0
        period = words[3]
        if prevp != period:
            y = -30
            r = random.randint(0, 255)
            g = random.randint(0, 230)
            b = random.randint(0, 200)

        idDisc = words[2]
        
        y = y + aux
        gexfPrint.write("<node id=\"" + idDisc + "\" label=\"" + idDisc + "\">\n")
        gexfPrint.write("<attvalues></attvalues>\n")
        gexfPrint.write("<viz:size value=\"2\"></viz:size>\n")
        sx = period + "9"
        
        if idDisc == "Admission":
            sx = "-10"
            sy = "-5"
            r = 0
            g = 0
            b = 0
        if idDisc == "Conclusion":
            xOfTheLastVertice = (noOfVertices * 2) + 30#depending on number of vertices of the particular graph
            sx = str(xOfTheLastVertice)
            sy = "-5"
            r = 0
            g = 0
            b = 0    
        gexfPrint.write("<viz:position x=\"" + sx + "\" y=\"" + sy + "\"></viz:position>\n")
        gexfPrint.write("<viz:color r=\"" + str(r) + "\" g=\"" + str(g) + "\" b=\"" + str(b) + "\"></viz:color>\n")
        gexfPrint.write("</node>\n") 
        prev = words [0] 
        noOfVertices = noOfVertices + 1
        prevp = period
    elif enter == True:
        if prev == "v":
                gexfPrint.write("</nodes>\n")
                gexfPrint.write("<edges>\n")
            
        gexfPrint.write("<edge id=\"" + str(ind) + "\" source=\"" + words[2] + "\" target=\"" + words[4] + "\" label=\"" + str(1) + "\">\n")
        gexfPrint.write("<attvalues></attvalues>\n")
        gexfPrint.write("</edge>\n")
        ind = ind +1
     
gexfPrint.write("</edges>\n")

gexfPrint.write("</graph>\n")
gexfPrint.write("</gexf>\n")
gexfPrint.close()
f.close()


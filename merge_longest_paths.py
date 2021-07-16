#merge the frequent longest paths of a particular curriculum
def check_if_new(filename,nodes_line):
    #return true if not present
    '''
    word = nodes_line.split("|")
    t = word[0]   
    h = open(str(filename),"r")
    lines = h.readlines()
    
    for line in lines:
        words = line.split("|")
        if words[0] == t:
            curr_line = " ".join(words)
            if curr_line == nodes_line:
                h.close()
                return False
            else:
                h.close()
                return True 
    '''
    h = open(str(filename),"r")
    lines = h.readlines()
    if nodes_line in lines:
        h.close()
        return False
    else :

        h.close()
        return True    
def merging():
    f = open("historicalLP.txt",'r')
    #g = open("dummy.txt")
    lines = f.readlines()
    #start = 0
    filename = ""
    for line in lines:
        words = line.split("|")
        
        if(words[0].upper()=="C"):
            if filename:    
                g.close()

            #assuming words[1] contains the curriculum id    
            filename = words[2].replace("\n","").replace(".","")+"_LongestPathsGraph.txt"
            g = open(str(filename),"a")

            #take the curriculum id and open the curriculum longest path merged file in append mode and close it after the last edge
        else:    
            nodes_line = "|".join(words)
            if(check_if_new(filename,nodes_line)):
                g.write(nodes_line)
            #write them as the nodes and edges if it is not already present in the file

if __name__=='__main__':
    merging()        
   
    

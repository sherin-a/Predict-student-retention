import Clustering
import sys
import os
from statistics import *

if __name__ == '__main__':
    c = Clustering.Clustering()
    
    g = open("LPonlyRetention.txt",'r') 
    
    lines = g.readlines()
    prev = ""
    distance = {}
    lines_stud = []
    formulas = ["3.3","3.4","3.5"]
    for line in lines:
        words = line.split("|")
        if words[0] == "g" or words[0] == "c":
                         
            if prev == "":
                prev = words[2].replace(".","").replace("\n",'')
            else:
                currFileName = prev + "_LongestPathsGraph.txt"
                f = open(currFileName,'r')
                lines_curr = f.readlines()
                #print("curriculum:"+str(prev))
                value = []
                value.append(c.find_distance_3_3(lines_curr,lines_stud))
                value.append(c.find_distance_3_4(lines_curr,lines_stud))
                value.append(c.find_distance_3_5(lines_curr,lines_stud))
                f.close()
                if prev not in distance:
                    distance[prev]=[]
                distance[prev].append(value)  
                prev = words[2].replace(".","").replace("\n",'')  
            lines_stud = []
        lines_stud.append(line)
    currFileName = prev + "_LongestPathsGraph.txt"
    f = open(currFileName,'r')
    lines_curr = f.readlines()
    value = []
    value.append(c.find_distance_3_3(lines_curr,lines_stud))
    value.append(c.find_distance_3_4(lines_curr,lines_stud))
    value.append(c.find_distance_3_5(lines_curr,lines_stud))
    f.close()
    if prev not in distance:
        distance[prev]=[]
    distance[prev].append(value)

    prev = words[2].replace(".","").replace("\n",'')     
    g.close()
    
   
    for curr in distance:
        #print(curr)
        #print("\n")
        #print(distance[curr])
        f = open(str(curr)+"_LongestPathsGraph.txt",'a')
        #print([item for elem in list(map(list,list(zip(distance[curr])))) for item in elem])
        #print(distance[curr])
        #print("Zipped\n")
        #print(list(zip(*distance[curr])))
        mean_list = list(map(mean,list(map(list,list(zip(*distance[curr]))))))
        median_list = list(map(median,list(map(list,list(zip(*distance[curr]))))))
        mode_list = list(map(mode,list(map(list,list(zip(*distance[curr]))))))
        #print(mean_list)
        #print(median_list)
        #print(mode_list)
        count = 0
        
        for i in formulas:
            f.write("Threshold_"+str(i))
            f.write("\nMean:"+str(mean_list[count]))
            f.write("\nMedian:"+str(median_list[count]))
            f.write("\nMode:"+str(mode_list[count]))
            f.write("\n")
            count = count +1
        
        f.close()
    
          
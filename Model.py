import Clustering
import sys
import os
from statistics import *

Threshold = {"3.3":{},"3.4":{},"3.5":{}}
def get_threshold(lines_curr):
    for line in lines_curr:
        words = line.split(':')
        words2 = line.split('_')
        if words2[0] == "Threshold":
            formula = words2[1].replace("\n","")
        if words[0] == "Mean":
            Threshold[formula]["Mean"] = float(words[1].replace("\n",""))
        if words[0] == "Mode":   
            Threshold[formula]["Mode"] = float(words[1].replace("\n",""))
        if words[0] == "Median":
            Threshold[formula]["Median"] = float(words[1].replace("\n",""))    

    return Threshold        
        #code using median and mode as well.Do it as per requirement	
def check_retention(lines_stud,curr):
    #get the corresponding curriculum graph
    curriculum_file = open( "flowchartLP.txt",'r')
    curriculum_file_lines = curriculum_file.readlines()
    sem_required = 0
    flag = False
    for line in curriculum_file_lines:
        words = line.split("|")
        if words[0] == "c" :
            if words[1].replace(".","").replace("\n",'') == curr:
                flag = True
            else:
                flag = False    
        if words[0] == "e" and flag== True:
            sem_required = int(words[5].replace("\n","")) + sem_required

    sem_taken = 0
    for line in lines_stud:
        words = line.split("|")
        if words[0] == "e":
            sem_taken = int(words[5].replace("\n","")) + sem_taken
    if sem_taken > sem_required	:
        return True
    else:
        return False		


if __name__ == '__main__':
    c = Clustering.Clustering()
   
    g = open("historical_testLP.txt",'r')
    lines = g.readlines()
    prev = ""
    formulas = ["3.3","3.4","3.5"]
    true_positive={}
    true_negative={}
    false_positive={}
    false_negative={}
    for value in formulas:
        true_positive[value]={"Mean":0,"Median":0,"Mode":0}
        true_negative[value]={"Mean":0,"Median":0,"Mode":0}
        false_positive[value]={"Mean":0,"Median":0,"Mode":0}
        false_negative[value]={"Mean":0,"Median":0,"Mode":0}
    
    lines_stud = []
    for line in lines:
        words = line.split("|")
        if words[0] == "g" or words[0] == "c":
                         
            if prev == "":
                prev = words[2].replace(".","").replace("\n",'')

            else:
                currFileName = prev + "_LongestPathsGraph.txt"
                f = open(currFileName,'r')
                lines_curr = f.readlines()
                
                get_threshold(lines_curr)
               
                #if threshold == None:
                 #   threshold = 1
                distance ={}
                distance["3.3"] = c.find_distance_3_3(lines_curr,lines_stud)
                distance["3.4"] = c.find_distance_3_4(lines_curr,lines_stud)
                distance["3.5"] = c.find_distance_3_5(lines_curr,lines_stud)
                f.close()
                Actual = check_retention(lines_stud,prev)
                for value in formulas:
                    for key in Threshold[value].keys():

                        if Threshold[value][key] == None:
                            Threshold[value][key] = 1
                        if distance[value]<=Threshold[value][key]:
                            #print("True " + str(Actual))
                            if Actual == True:
                                true_positive[value][key] = true_positive[value][key] + 1
                            if Actual == False:
                                false_positive[value][key] = false_positive[value][key] + 1	
                        
                        else :
                            #print("False " + str(Actual))

                            if Actual == True:
                                false_negative[value][key] = false_negative[value][key] + 1
                            if Actual == False:
                                true_negative[value][key] = true_negative[value][key] + 1	

                prev = words[2].replace(".","").replace("\n",'')  
            lines_stud = []
        lines_stud.append(line)
    g.close()
    for value in formulas:
        for key in Threshold[value].keys():
            print("\nAccuracy measures using "+str(key)+" for formula:"+str(value)+"\n")
            precision = float(true_positive[value][key]/(true_positive[value][key]+false_positive[value][key]))
            recall = float(true_positive[value][key]/(true_positive[value][key]+false_negative[value][key]))
            print ("True positive:"+str(true_positive[value][key]))
            print ("\nFalse positive:"+str(false_positive[value][key]))
            print("\nTrue Negative:"+str(true_negative[value][key]))
            print("\nFalse Negative:"+str(false_negative[value][key]))
            
            print("Precision:"+str(precision))
            print("\nRecall:"+str(recall)+"\n")
   

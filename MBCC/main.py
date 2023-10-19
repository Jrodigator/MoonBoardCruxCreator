#import keras as k  
import numpy as np 
import os 
import pandas as pd
from PIL import Image

############################

dataDir = "/RoutePics/Bench/"

############################

gradeDict = [

    [0, '3', 0],
    [1, '4', 0],
    [2, '5A', 0],
    [3, '5B', 0],
    [4, '5C', 0],
    [5, '6A', 0],
    [6, '6A+', 0],
    [7, '6B', 0],
    [8, '6B+', 0],
    [9, '6C', 0],
    [10, '6C+', 0],
    [11, '7A', 0],
    [12, '7A+', 0],
    [13, '7B', 0],
    [14, '7B+', 0],
    [15, '7C', 0],
    [16, '7C+', 0],
    [17, '8A', 0],
    [18, '8A+', 0],
    [19, '8B', 0],
    [20, '8B+', 0],
    [21, '8C', 0],

]


def scanFolder(directory): 

    dataSet = [[]]
    for filename in os.listdir(directory):  
        file = os.fsdecode(filename)
        if file.endswith(".png"): 

            # print(os.path.join(directory, filename))  

            grade = filename[::-1].split('.')[1]  # flip and remove extention
            grade = grade.split('_')[0]  # remove the rest of the name
            grade = grade[::-1]  # flip back

            climb = filename[::-1].split('.')[1]  # flip and remove extention
            climb = climb.split('_')[1]  # remove the rest of the name
            climb = climb[::-1]  # flip back

            data = Image.open(directory + filename)
            data = np.array(data)

            dataSet.append((filename, climb, grade, data))
        else:  
            continue
            # scanFolder(os.path.join
    return dataSet

    print(dataSet)

def countClimbs(set):
    count = [] #np.array(gradeDict)
    
    for k in range(len(gradeDict)):
        count.append((gradeDict[k][1], 0))

    for i in range(len(set)):
        for j in range(len(gradeDict)):
            
            # print(j)
            # print(set[i][2], count[j][0])
            
            if set[i][2] == count[j][0]:
                count[j] = (count[j][0], count[j][1] + 1)
    
    return count


        

def main():
    
    # Load the data
    dataSet = scanFolder(dataDir)
    dataSet.pop(0)  # remove the first empty list
    # print(dataSet[0])
    print(countClimbs(dataSet))

    return 0 


main()
    
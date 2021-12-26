import random 
#import numpy as np

numberArray = [[1,2,3],[4,5,6],[7,8,9]]
#for i in range(9):
#    numberArray().append(i+1)
    
trialNumber = 1
#print(numberArray)
value = 0
while not (value == 1):
    random.shuffle(numberArray)
    print("Trial ", trialNumber)
    for x in range(3):
        print(numberArray[x])
    if numberArray[0][0] + numberArray[0][1] + numberArray[0][2] == 15:
        if numberArray[1][0] + numberArray[1][1] + numberArray[1][2] == 15:
            if numberArray[2][0] + numberArray[2][1] + numberArray[2][2] == 15:
                if numberArray[1][0] + numberArray[2][0] + numberArray[3][0] == 15:
                    if numberArray[1][1] + numberArray[2][1] + numberArray[3][1] == 15:
                        if numberArray[1][2] + numberArray[2][2] + numberArray[3][2] == 15:
                            value = 1; 




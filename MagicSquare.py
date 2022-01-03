import random 
from threading import Thread
import numpy as np

def main():
    numberArray=[]
    for i in range(9):
        numberArray.append(i+1)
    checkSquare(numberArray)
    print("Magic Square Has Been Found on ")


def createSquare(magicSquare):
    
    random.shuffle(magicSquare)
    npMagicSquare = np.array(magicSquare)
    npMagicSquare = np.reshape(npMagicSquare, (3,3))
    print(npMagicSquare)
    

def checkSquare(magicSquare):
    value = 1
    trial = 1
    while not (value ==0):
        trial += 1
        print("trial Number: ", trial)
        
        createSquare(magicSquare)
        if sum(magicSquare[0:2]) == 15 and sum(magicSquare[3:5])==15 and sum(magicSquare[6:8])==15:
            if magicSquare[0] + magicSquare[3] + magicSquare[6] ==15 and magicSquare[1] + magicSquare[4] + magicSquare[7] ==15 and magicSquare[2] + magicSquare[5] + magicSquare[8] ==15:
                if magicSquare [0] + magicSquare[4] + magicSquare[8] ==15 and magicSquare[2] + magicSquare[4] + magicSquare [6] ==15: 
                    value = 0
    print("Magic Square Has Been Found on Trial ", trial)


if __name__ == "__main__":
    main()
























# numberArray = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(9):
#     numberArray().append(i+1)

#print(numberArray)
#value = 0
# def MagicSquare():



# value = 0
# trialNumber = 1
# while not (value == 1):
#     random.shuffle(numberArray)
#     print("Trial ", trialNumber)
#     trialNumber += 1
#     # if trialNumber >= 25000000:
#     #      numberArray = [[2,7,6],[9,5,1],[4,3,8]];
#     for x in range(3):
#         print(numberArray[x])
#     if numberArray[0][0] + numberArray[0][1] + numberArray[0][2] == 15:
#         if numberArray[1][0] + numberArray[1][1] + numberArray[1][2] == 15:
#             if numberArray[2][0] + numberArray[2][1] + numberArray[2][2] == 15:
#                 if numberArray[0][0] + numberArray[1][0] + numberArray[2][0] == 15:
#                     if numberArray[0][1] + numberArray[1][1] + numberArray[2][1] == 15:
#                         if numberArray[0][2] + numberArray[1][2] + numberArray[2][2] == 15:
#                             value = 1; 
# print("Magic Square found at trial ", trialNumber, "!")
# 
# 
# 
# 
# 
# MagicSquare
# if __name__ == "__main__":
#     Thread(target = MagicSquare).start()
#     Thread(target = MagicSquare).start()
#     Thread(target = MagicSquare).start()
#     Thread(target = MagicSquare).start()

    # t1 = threading.Thread(target=MagicSquare,args=(0,))
    # t2 = threading.Thread(target=MagicSquare,args=(0,))
    # t3 = threading.Thread(target=MagicSquare,args=(0,))

    # t1.start()
    # t2.start()
    # t3.start()

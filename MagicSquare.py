import random 
from threading import Thread
import numpy as np

def main():
    numberArray=[]
    for i in range(9):
        numberArray.append(i+1)
    checkSquare(numberArray)


def createSquare(magicSquare):
    
    random.shuffle(magicSquare)
    npMagicSquare = np.array(magicSquare)
    npMagicSquare = np.reshape(npMagicSquare, (3,3))
    print(npMagicSquare)
    

def checkSquare(magicSquare):
    value = 1
    trial = 1
    while not (value ==0):
        print("trial Number: ", trial)
        trial += 1
        createSquare(magicSquare)
        # if trial >= 10000:
        #     magicSquare = [2,7,6,9,5,1,4,3,8]
        if magicSquare[0]+magicSquare[1]+magicSquare[2] == 15 and magicSquare[3] + magicSquare[4] + magicSquare[5]==15 and magicSquare[6] + magicSquare[7] + magicSquare[8]==15:
            if magicSquare[0] + magicSquare[3] + magicSquare[6] ==15 and magicSquare[1] + magicSquare[4] + magicSquare[7] ==15 and magicSquare[2] + magicSquare[5] + magicSquare[8] ==15:
                if magicSquare [0] + magicSquare[4] + magicSquare[8] ==15 and magicSquare[2] + magicSquare[4] + magicSquare [6] ==15: 
                    value = 0

    print("Magic Square Has Been Found on Trial", trial)


if __name__ == "__main__":
    main()
























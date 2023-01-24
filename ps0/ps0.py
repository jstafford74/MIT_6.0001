import numpy as np

numX = int(input("Enter number x:"))
numY = int(input("Enter number y:"))
numPower = numX**numY
numLog = np.log2(numX)
print("X**y =",numPower)
print("log(x) =",numLog)
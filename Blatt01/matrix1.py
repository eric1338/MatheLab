print("matrix1 [Ex. 1.1 a-c)]")

import mylib;
import numpy as np;

def getVectorFromLine(line):
    numbers = []
    numberString = ""
    for c in line:
        if c == ' ' or c == ';':
            numbers.append(float(numberString))
            numberString = ""
        else:
            numberString += c
    
    return numbers


def swapMatrixRows(matrix, row1, row2):
    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp


myMatrix = []
myVector = []

textFile = open('matrixTextFile.txt', 'r')

readMatrix = True

for line in textFile:
    if len(line) > 0:
        if line[0] == '#':
            readMatrix = False
        else:
            vectorRead = getVectorFromLine(line)
            
            if readMatrix: myMatrix.append(vectorRead)
            else: myVector = vectorRead

print("Matrix from file:")
mylib.printMatrix(myMatrix)

print(" ")
print("Vector from file:")
mylib.printVector(myVector)

matrixArr = np.array(myMatrix)
vectorArr = np.array(myVector)

print(" ")
print("a)")
print("determinant:")

detA = np.linalg.det(matrixArr)
print(detA)

print(" ")
print("inverse:")

invA = np.linalg.inv(matrixArr)
mylib.printMatrix(invA)

print(" ")
print("rank:")

rankA = np.linalg.matrix_rank(matrixArr)
print(rankA)

print(" ")
print("eigen?")

eigA = np.linalg.eig(matrixArr)
print(eigA)

print(" ")
print("is symmetric:")

isSym = (matrixArr.transpose() == matrixArr).all()
print(isSym)

print(" ")
print("is positive definite:")

isPosDef = np.all(np.linalg.eigvals(matrixArr))
print(isPosDef)

print(" ")
print("b)")

linSolutions = np.linalg.solve(matrixArr, vectorArr)

xNum = 1;

for linSolution in linSolutions:
	print("x" + str(xNum) + " = " + str(linSolution))
	xNum += 1


# checks evtl davor (eigene Funktion?)


def gaussElemMethod(matrix, vector):
	n = len(matrix[0])
	
	for k in range(n - 1):
		maxL = -1
		for l in range(k, n):
			maxL = max(maxL, abs(matrix[l][k]))
		
		mFound = -1
		
		for m in range(n):
			if abs(matrix[m][k]) == maxL:
				mFound = m
		
		if mFound > 0 and matrix[mFound][k] == 0:
			print("singular")
			continue
		
		swapMatrixRows(matrix, mFound, k)
		
		for i in range(k + 1, n):
			qik = matrix[i][k] / matrix[k][k]
			
			for j in range(0, n):
				matrix[i][j] = matrix[i][j] - qik * matrix[k][j]
			
			vector[i] = vector[i] - qik * vector[k]



gaussElemMethod(myMatrix, myVector)

print(" ")
print("c)")
print("matrix after elimination:")
mylib.printMatrix(myMatrix)

print(" ")
print("vector after elimination:")
mylib.printVector(myVector)

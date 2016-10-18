print("matrix1 [Ex. 1.1 a-c)]")

textFile = open('matrixTextFile.txt', 'r')

readMatrix = True

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


def myPrintVector(vector):
    for element in vector:
        print(element)


def myPrintMatrix(matrix):
    for row in matrix:
        rowStr = ""
        for element in row:
            rowStr += str(element) + " "
        print(rowStr)


def swapMatrixRows(matrix, row1, row2):
    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp


myMatrix = []
myVector = []

for line in textFile:
    if len(line) > 0:
        if line[0] == '#':
            readMatrix = False
        else:
            vectorRead = getVectorFromLine(line)
            
            if readMatrix: myMatrix.append(vectorRead)
            else: myVector = vectorRead

print("Matrix")
myPrintMatrix(myMatrix)

print("Vector")
myPrintVector(myVector)

swapMatrixRows(myMatrix, 0, 2)
myPrintMatrix(myMatrix)

# checks evtl davor (eigene Funktion?)

n = len(myMatrix[0])


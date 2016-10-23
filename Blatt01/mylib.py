
def getNumberString(pNumber, strLength):
	nStr = str(round(pNumber, 2))
	
	if pNumber >= 0: nStr = " " + nStr
	
	spacesBefore = strLength - len(nStr)
	
	if spacesBefore > 0:
		for i in range(spacesBefore): nStr = " " + nStr
	
	return nStr


def printVector(pVector):
    for element in pVector:
        print(getNumberString(element, 7))


def printMatrix(pMatrix):
    for row in pMatrix:
        rowStr = ""
        for element in row:
            rowStr += getNumberString(element, 7) + " "
        print(rowStr)


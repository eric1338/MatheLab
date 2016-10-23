print("matrix2 [Ex. 1.2 a-b)]")

import mylib;

print("a)")

matrix1 = [[1.8, -2], [3, -4.1], [3, 2]]
matrix2 = [[1, -2, -3, 1], [-5, 4, 1, 1]]

print("matrix A:")
mylib.printMatrix(matrix1)

print(" ")
print("matrix B:")
mylib.printMatrix(matrix2)

print(" ")
print("A x B:")

matrix1Rows = len(matrix1)
matrix2Rows = len(matrix2)

matrix1Cols = len(matrix1[0])
matrix2Cols = len(matrix2[0])

resultMatrix = []

if matrix1Cols != matrix2Rows:
	print("nicht uebereinstimmend")

for matrix1Row in range(matrix1Rows):

	resultVector = []
	for matrix2Col in range(matrix2Cols):
		
		mySum = 0
		
		for k in range(matrix1Cols):
			mySum = mySum + matrix1[matrix1Row][k] * matrix2[k][matrix2Col]
		
		resultVector.append(mySum)
		
	resultMatrix.append(resultVector)

mylib.printMatrix(resultMatrix)

print(" ")
print("b)")

matrix3 = [[1, 2.4], [3.3, -4], [-5, -6.1]]

print("matrix C:")
mylib.printMatrix(matrix3)

matrix3Rows = len(matrix3)
matrix3Cols = len(matrix3[0])

transposedMatrix = []

for j in range(matrix3Cols):
	transposedVector = []

	for i in range(matrix3Rows):
		transposedVector.append(matrix3[i][j])
	
	transposedMatrix.append(transposedVector)

print(" ")
print("C transposed:")
mylib.printMatrix(transposedMatrix)

print("matrix multiplication [Ex. 1.2 a)+b)]")

print("a)")

m1 = [[1, 2], [3, 4], [5, 6]]
m2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

m1Rows = len(m1)
m2Rows = len(m2)

m1Cols = len(m1[0])
m2Cols = len(m2[0])

if m1Cols != m2Rows:
	print("nicht uebereinstimmend")

for m1Row in range(m1Rows):

	rowStr = "";
	for m2Col in range(m2Cols):
		
		mySum = 0
		
		for k in range(m1Cols):
			mySum = mySum + m1[m1Row][k] * m2[k][m2Col]
		
		rowStr += (str(mySum) + "  ")
		
	print(rowStr)

print(" ")
print("b)")
#m3 = [[1, 2], [3, 4], [5, 6]]
#m3 = [[1, 3, 5], [2, 4, 6]]

m3Rows = len(m3)
m3Cols = len(m3[0])

for j in range(m3Cols):
	rowStr = ""

	for i in range(m3Rows):
		rowStr += str(m3[i][j]) + "  "
		
	print(rowStr)
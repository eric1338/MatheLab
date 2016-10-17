print("fibonacci [Ex. 2.3 c)+d)]")

import time;

print("c)")

def fibonacciFunc(x):
	if x <= 1: return 1
	
	return fibonacciFunc(x - 1) + fibonacciFunc(x - 2)

def myPlot(plotList):
	maxValue = -1
	for i in plotList:
		if i > maxValue: maxValue = i
	
	yRange = 20;
	
	yStep = maxValue / yRange
	
	print(maxValue)
	
	for row in range(20):
		yVal = yStep * (yRange - row)
		
		rowStr = "";
	
		for res in plotList:
			if abs(res - yVal) < yStep: rowStr += "x"
			else: rowStr += " "
		print(rowStr)
	print("0")

results = []

for i in range(20):
	fib = fibonacciFunc(i)
	print("fib(" + str(i + 1) + "): " + str(fib))
	results.append(fib)
	

print(" ")
print("d)")

runtimes = []

for i in range(32):
	timeStart = time.time()
	fibonacciFunc(i)
	ms = 1000 * (time.time() - timeStart)
	runtimes.append(ms)

myPlot(runtimes)

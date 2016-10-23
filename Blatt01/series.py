print("series [Ex. 2.4 a-c)]")

import math;
import matplotlib.pyplot as plt

def factorialFunc(x):
    if x <= 0: return 1
	
    return x * factorialFunc(x - 1)


def aFunc(x):
	sum = 0
	for i in range(x):
		sum += (1.0 / factorialFunc(i))
	return sum

results = []
eulers = []

for i in range(10):
	results.append(aFunc(i))
	eulers.append(math.e)


print("a)")

plt.plot(results)
plt.plot(eulers)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(" ")
print("b)")

def sinDerive(d):
	xMod = d % 4
	if (xMod == 0): return 0
	if (xMod == 1): return 1
	if (xMod == 2): return 0
	return -1


#	if (xMod == 0): return math.sin(x)
#	if (xMod == 1): return math.cos(x)
#	if (xMod == 2): return -math.sin(x)
#	return -math.cos(x)

def bFunc(d, x):
	sum = 0
	for i in range(d):
		sum += (sinDerive(i + 1) / factorialFunc(i + 1)) * pow(x, d)
	
	return sum

def bFunc2(d):
	pi = 3.1415926
	nSteps = 40
	xStep = 4 * pi / nSteps
	x = pi * -2
	
	results = []
	
	for i in range(nSteps):
		results.append(bFunc(d, x))
		x += xStep
	
	#myPlot(results)

for i in range(6):
	print("degree: " + str(i + 1))
	bFunc2(i + 1)
	print(" ")


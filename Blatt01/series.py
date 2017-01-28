print("series [Ex. 2.4 a-c)]")

import math;
import matplotlib.pyplot as plt;

def factorialFunc(x):
    if x <= 0: return 1;
	
    return x * factorialFunc(x - 1);


def aFunc(x):
	sum = 0
	for i in range(x):
		sum += (1.0 / factorialFunc(i));
	return sum;

results = [];
eulers = [];

for i in range(10):
	results.append(aFunc(i));
	eulers.append(math.e);


print("a)");

plt.plot(results);
plt.plot(eulers);
plt.xlabel('x');
plt.ylabel('y');
plt.show();


print(" ")
print("b)")

def bFunc(d, x):
	sum = x;
	
	if (d >= 3): sum -= (1.0 / 6.0) * pow(x, 3);
	
	if (d >= 5): sum += (1.0 / 120.0) * pow(x, 5);
	
	return sum;


def bFunc2(d):
	nSteps = 40;
	xStep = 4 * math.pi / (nSteps - 1);
	x = math.pi * -2;
	
	xses = [];
	results = [];
	
	for i in range(nSteps):
		xses.append(x);
		results.append(bFunc(d, x));
		x += xStep;
	
	return [xses, results];


for i in range(0, 7):
	taylorFunc = bFunc2(i);
	plt.plot(taylorFunc[0], taylorFunc[1]);

plt.xlabel('x');
plt.ylabel('y');
plt.show();


print(" ");
print("c)");

def eulerFunc(d, x):
	if (d <= 0): return 1;

	sum = 1;
	
	for i in range(1, d + 1):
		sum += pow(x, i) / (factorialFunc(i) + 0.0);
	
	return sum;


def getRemainder(n, x):
	xabs = abs(x);
	
	return (math.exp(xabs) * pow(xabs, n + 1)) / (factorialFunc(n + 1) + 0.0);


def getDegree(x):
	n = 0;
	
	while n < 100:
		remainder = getRemainder(n, x);
		
		if (remainder < 1e-11): return n;
		
		n = n + 1;
		
	return -1;


for x in range(1, 6):
	deg = getDegree(x);
	eul = eulerFunc(deg, x);
	
	print("x = " + str(x) + " | degree = " + str(deg) + " | e(" + str(x) + ") = " + str(eul));

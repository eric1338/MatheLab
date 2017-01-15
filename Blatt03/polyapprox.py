print("polynomial approximation 1 [Ex. 5.9 a-d)]")

import math;
import matplotlib.pyplot as plt;
import numpy as np;


def getCoefficients(fx, degree, a, b):
	valA = fx(a);
	valB = fx(b);
	
	xses = [];
	yses = [];
	
	step = (b - a) / float(degree - 1);
	
	for i in range(degree):
		x = a + i * step;
		xses.append(x);
		yses.append(fx(x));
	
	matA = [];
	
	for xVal in xses:
		row = [];
		for i in range(degree):
			row.append(pow(xVal, i));
		
		matA.append(row);
	
	matrixArr = np.array(matA);
	vectorArr = np.array(yses);
	
	linSolutions = np.linalg.solve(matrixArr, vectorArr);
	
	return linSolutions;



def polynomialF(coefficients, x):
	sum = 0.0;
	
	for i in range(len(coefficients)):
		sum += coefficients[i] * pow(x, i);
	
	return sum;



def myF(x):
	return pow(math.e, -pow(x, 2));



def taylorFuncAt0(x):
	sum = 1;
	sum -= pow(x, 2);
	sum += pow(x, 4) / 2.0;
	sum -= pow(x, 6) / 6.0;
	sum += pow(x, 8) / 24.0;
	sum -= pow(x, 10) / 120.0;
	sum += pow(x, 12) / 720.0;
	sum -= pow(x, 14) / 5040.0;
	sum += pow(x, 16) / 40320.0;
	
	return sum;



def taylorFuncAt4(x):
	ep16 = float(pow(math.e, 16));
	xm4 = x - 4;
	
	sum = 1 / ep16;
	sum -= 8 * xm4 / ep16;
	sum += 31 * pow(xm4, 2) / ep16;
	sum -= 232 * pow(xm4, 3) / (3 * ep16);
	sum += 835 * pow(xm4, 4) / (6 * ep16);
	sum -= 2876 * pow(xm4, 5) / (15 * ep16);
	sum += 18833 * pow(xm4, 6) / (90 * ep16);
	sum -= 58076 * pow(xm4, 7) / (315 * ep16);
	sum += 332777 * pow(xm4, 8) / (2520 * ep16);
	sum -= 43325 * pow(xm4, 9) / (567 * ep16);
	sum += 3937007 * pow(xm4, 10) / (113400 * ep16);
	
	return sum;



print("b)");

coefficients = getCoefficients(myF, 10, -2, 10);

xses = [];
realYses = [];
approxYses = [];
taylor0Yses = [];
taylor4Yses = [];

for i in range(100):
	x = -2 + i * (12 / 100.0);
	
	xses.append(x);
	realYses.append(myF(x));
	approxYses.append(polynomialF(coefficients, x));
	taylor0Yses.append(taylorFuncAt0(x));
	taylor4Yses.append(taylorFuncAt4(x));


plt.plot(xses, realYses);
plt.plot(xses, approxYses);
plt.xlabel('x');
plt.ylabel('y');
plt.show();


print(" ");
print("c)");

maxApproxDev = -1;
maxTaylor0Dev = -1;
maxTaylor4Dev = -1;

for i in range(100):
	realY = realYses[i];
	approxY = approxYses[i];
	taylor0Y = taylor0Yses[i];
	taylor4Y = taylor4Yses[i];
	
	maxApproxDev = max(maxApproxDev, abs(realY - approxY));
	maxTaylor0Dev = max(maxTaylor0Dev, abs(realY - taylor0Y));
	maxTaylor4Dev = max(maxTaylor4Dev, abs(realY - taylor4Y));


print("maximum deviation: " + str(maxApproxDev));


print(" ");
print("d)");

print("maximum deviation of taylor series with c = 0: " + str(maxTaylor0Dev));
print("maximum deviation of taylor series with c = 4: " + str(maxTaylor4Dev));


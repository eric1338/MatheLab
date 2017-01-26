print("method of least squares 2 [Ex. 5.11 a-f)]")

import math;
import random;
import matplotlib.pyplot as plt;
import numpy as np;
import sys;


def getCoefficients(baseFunctions, dataPoints):
	l = len(baseFunctions);
	
	matA = [];
	
	for i in range(l):
		matrixRow = [];
		for j in range(l):
			elemSum = 0;
		
			for dp in dataPoints:
				x = dp[0];
				elemSum += baseFunctions[i](x) * baseFunctions[j](x);
			
			matrixRow.append(elemSum);
		
		matA.append(matrixRow);
	
	vecB = [];
	
	for i in range(l):
		elemSum = 0;
	
		for dp in dataPoints:
			elemSum += dp[1] * baseFunctions[i](dp[0]);
		
		vecB.append(elemSum);
	
	
	matrixArr = np.array(matA);
	vectorArr = np.array(vecB);
	
	linSolutions = np.linalg.solve(matrixArr, vectorArr);
	
	return linSolutions;
#


def myF8(x): return pow(x, 8);

def myF7(x): return pow(x, 7);

def myF6(x): return pow(x, 6);

def myF5(x): return pow(x, 5);

def myF4(x): return pow(x, 4);

def myF3(x): return pow(x, 3);

def myF2(x): return pow(x, 2);

def myF1(x): return x;

def myF0(x): return 1;


def getBaseFunctionList(degree):
	baseFunctions = [];
	
	if degree >= 8: baseFunctions.append(myF8);
	if degree >= 7: baseFunctions.append(myF7);
	if degree >= 6: baseFunctions.append(myF6);
	if degree >= 5: baseFunctions.append(myF5);
	if degree >= 4: baseFunctions.append(myF4);
	if degree >= 3: baseFunctions.append(myF3);
	if degree >= 2: baseFunctions.append(myF2);
	
	baseFunctions.append(myF1);
	baseFunctions.append(myF0);
	
	return baseFunctions;
#

def polynomialF(coefficients, x):
	sum = 0.0;
	
	nc = len(coefficients);
	
	for i in range(nc):
		sum += coefficients[i] * pow(x, nc - i - 1);
	
	return sum;
#


txtPoints = [];

txtPoints.append([8, -16186.1]);
txtPoints.append([9, -2810.82]);
txtPoints.append([10, 773.875]);
txtPoints.append([11, 7352.34]);
txtPoints.append([12, 11454.5]);
txtPoints.append([13, 15143.3]);
txtPoints.append([14, 13976.]);
txtPoints.append([15, 15137.1]);
txtPoints.append([16, 10383.4]);
txtPoints.append([17, 14471.9]);
txtPoints.append([18, 8016.53]);
txtPoints.append([19, 7922.01]);
txtPoints.append([20, 4638.39]);
txtPoints.append([21, 3029.29]);
txtPoints.append([22, 2500.28]);
txtPoints.append([23, 6543.8]);
txtPoints.append([24, 3866.37]);
txtPoints.append([25, 2726.68]);
txtPoints.append([26, 6916.44]);
txtPoints.append([27, 8166.62]);
txtPoints.append([28, 10104.]);
txtPoints.append([29, 15141.8]);
txtPoints.append([30, 15940.5]);
txtPoints.append([31, 19609.5]);
txtPoints.append([32, 22738.]);
txtPoints.append([33, 25090.1]);
txtPoints.append([34, 29882.6]);
txtPoints.append([35, 31719.7]);
txtPoints.append([36, 38915.6]);
txtPoints.append([37, 37402.3]);
txtPoints.append([38, 41046.6]);
txtPoints.append([39, 37451.1]);
txtPoints.append([40, 37332.2]);
txtPoints.append([41, 29999.8]);
txtPoints.append([42, 24818.1]);
txtPoints.append([43, 10571.6]);
txtPoints.append([44, 1589.82]);
txtPoints.append([45, -17641.9]);
txtPoints.append([46, -37150.2]);


evenPoints = [];

for txtPoint in txtPoints:
	if txtPoint[0] % 2 == 0:
		evenPoints.append(txtPoint);


matrixX = [];
matrixT = [];

for evenPoint in evenPoints:
	rnd = random.random();
	
	if len(matrixT) >= 10 or (rnd < 0.5 and len(matrixX) < 10):
		matrixX.append(evenPoint);
	else:
		matrixT.append(evenPoint);



print("c)");

allYses = [];

xses = [];

for i in range(152):
	xses.append(8 + i * 0.25);


for i in range(7):
	degree = i + 2;
	
	baseFunctionList = getBaseFunctionList(degree);
	
	coefficients = getCoefficients(baseFunctionList, matrixX);
	
	yses = [];
	
	for x in xses:
		y = polynomialF(coefficients, x);
		yses.append(y);
	
	allYses.append(yses);


xXses = [];
xYses = [];
tXses = [];
tYses = [];

for i in range(10):
	xXses.append(matrixX[i][0]);
	xYses.append(matrixX[i][1]);
	tXses.append(matrixT[i][0]);
	tYses.append(matrixT[i][1]);


#colors = ["r", "g", "b", "c", "m", "y", "k"];
colors = ["b", "c", "r", "g", "m", "y", "k"];


plt.plot(xXses, xYses, "bo");
plt.plot(tXses, tYses, "ro");

for i in range(len(allYses)):
	plt.plot(xses, allYses[i], colors[i]);

plt.xlabel("x");
plt.ylabel("y");
plt.show();


print(" ");
print("d)");

def getError(coefficients, mat):
	errorSum = 0;
	
	for elem in mat:
		fY = polynomialF(coefficients, elem[0]);
		
		errorSum += pow(fY - elem[1], 2);
	
	return errorSum;
#

def getErrors(degree, matX, matT):
	baseFunctionList = getBaseFunctionList(degree);
	
	coefficients = getCoefficients(baseFunctionList, matX);
	
	errorSumX = getError(coefficients, matX);
	errorSumT = getError(coefficients, matT);
	
	return [errorSumX, errorSumT];
#

degrees = [];
errorsX = [];
errorsT = [];

for i in range(7):
	degree = i + 2;
	
	degrees.append(degree);
	
	errors = getErrors(degree, matrixX, matrixT);
	
	errorsX.append(errors[0]);
	errorsT.append(errors[1]);
#

plt.plot(degrees, errorsX, "b");
plt.plot(degrees, errorsT, "r");

plt.xlabel("degree");
plt.ylabel("error");
plt.show();














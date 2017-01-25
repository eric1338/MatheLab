print("method of least squares 1 [Ex. 5.10 a-d)]")

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


def myF4(x): return pow(x, 4);

def myF3(x): return pow(x, 3);

def myF2(x): return pow(x, 2);

def myF1(x): return x;

def myF0(x): return 1;

def myF(a, x, n): return a * pow(x, n);



def polynomialF(coefficients, x):
	sum = 0.0;
	
	nc = len(coefficients);
	
	for i in range(nc):
		sum += coefficients[i] * pow(x, nc - i - 1);
	
	return sum;
#


print("b)");

baseFns = [];

baseFns.append(myF1);
baseFns.append(myF0);

linPoints = [];
rndPoints = [];
xses = [];
yses = [];
rndYses = [];

for i in range(100):
	x = i / 10.0;
	y = x * 0.64 + 2.3;
	
	xses.append(x);
	yses.append(y);

	rnd = random.random() - 0.5;
	rndY = y + rnd * 0.6;
	rndYses.append(rndY);
	
	linPoints.append([x, y]);
	rndPoints.append([x, rndY]);


print("coefficients:");
print(getCoefficients(baseFns, linPoints));

print(" ");
print("approximated coefficients:");
print(getCoefficients(baseFns, rndPoints));


plt.plot(xses, yses);
plt.plot(xses, rndYses, "ro");
plt.xlabel("x");
plt.ylabel("y");
plt.show();


print(" ");
print("d)");

txtBaseFns4 = [];
txtBaseFns2 = [];

txtBaseFns4.append(myF4);
txtBaseFns4.append(myF3);
txtBaseFns4.append(myF2);
txtBaseFns4.append(myF1);
txtBaseFns4.append(myF0);

txtBaseFns2.append(myF2);
txtBaseFns2.append(myF1);
txtBaseFns2.append(myF0);

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

txtCoefficients4 = getCoefficients(txtBaseFns4, txtPoints);
txtCoefficients2 = getCoefficients(txtBaseFns2, txtPoints);

txtPointsXses = [];
txtPointsYses = [];

error4 = 0;
error2 = 0;

for i in range(len(txtPoints)):
	txtPoint = txtPoints[i];
	
	txtPointsXses.append(txtPoint[0]);
	txtPointsYses.append(txtPoint[1]);
	
	y4 = polynomialF(txtCoefficients4, i + 8);
	y2 = polynomialF(txtCoefficients2, i + 8);
	
	error4 += pow(y4 - txtPoint[1], 2);
	error2 += pow(y2 - txtPoint[1], 2);


print("error of degree 4 polynomial: " + str(error4));
print("error of degree 2 polynomial: " + str(error2));

txtFXses = [];
txtF4Yses = [];
txtF2Yses = [];

for i in range(152):
	x = 8 + i * 0.25;
	
	txtFXses.append(x);
	
	y4 = polynomialF(txtCoefficients4, x);
	y2 = polynomialF(txtCoefficients2, x);
	
	txtF4Yses.append(y4);
	txtF2Yses.append(y2);


plt.plot(txtFXses, txtF4Yses);
plt.plot(txtFXses, txtF2Yses);
plt.plot(txtPointsXses, txtPointsYses, "ro");
plt.xlabel("x");
plt.ylabel("y");
plt.show();


print("roots [Ex. 4.8 a-f)]")

import math;
import time;
import matplotlib.pyplot as plt;


def fFixed(x):
	return 0.5 * pow(math.e, -pow(x, 2));


def f(x):
	return fFixed(x) - x;


def fDerived(x):
	return -pow(math.e, -pow(x, 2)) * x;



print("a)");

xses = [];
fLeft = [];
fRight = [];

for i in range(200):
	x = (i / 100.0) - 1;
	
	xses.append(x);
	fLeft.append(fFixed(x));
	#fLeft.append(0.5 * pow(math.e, -pow(x, 2)));
	fRight.append(x);


plt.plot(xses, fLeft);
plt.plot(xses, fRight);
plt.xlabel('x');
plt.ylabel('y');
#plt.show();



	

def mySign(x):
	return -1 if x < 0 else 1;



def getRootBisectionRec(xa, xb, maxSteps, stepsTaken):
	xm = xa + (xb - xa) / 2;
	
	if stepsTaken >= maxSteps: return xm;
	
	newXA = xa;
	newXB = xb;
	
	if mySign(f(xa)) != mySign(f(xm)):
		newXB = xm;
	else:
		newXA = xm;

	return getRootBisectionRec(newXA, newXB, maxSteps, stepsTaken + 1);


def getRootBisection(xa, xb, maxSteps):
	if mySign(f(xa)) == mySign(f(xb)):
		print("fail");
		return -1;
	
	return getRootBisectionRec(xa, xb, maxSteps, 0);



def getRootNewtonRec(x, maxSteps, stepsTaken):
	fD = fDerived(x);
	
	if abs(fD) < 0.00001: fD = 0.00001;
	
	nextX = x - (f(x) / fD);
	
	if stepsTaken < maxSteps:
		return getRootNewtonRec(nextX, maxSteps, stepsTaken + 1)
	else:
		return nextX;


def getRootNewton(x0, maxSteps):
	return getRootNewtonRec(x0, maxSteps, 0);



def getFixedPointRec(x, maxSteps, stepsTaken):
	newX = fFixed(x);
	
	if stepsTaken < maxSteps:
		return getFixedPointRec(newX, maxSteps, stepsTaken + 1);
	else:
		return newX;


def getFixedPoint(x0, maxSteps):
	return getFixedPointRec(x0, maxSteps, 0);



def getTime():
	return time.time();

def printTimeDiff(startTime, endTime):
	diff = endTime - startTime;
	print("diff: " + str(diff));


print(" ");
print("b)");

rootBisection = getRootBisection(0.01, 1, 10);
rootNewton = getRootNewton(0.5, 10);

print(rootBisection);
print(rootNewton);

fixedPoint = getFixedPoint(0, 10);

print(fixedPoint);
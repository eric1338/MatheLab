print("monte-carlo methods [Ex. 7.12 a-c)]")

import math;
import random;
import matplotlib.pyplot as plt;


def getRandCoord(a, b):
	return random.random() * (b - a) + a;
#

def circleF(x):
	newX = (x % 2) - 1;
	return math.sqrt(1 - pow(newX, 2));
#

def doNaiveMonteCarloTest(xMin, xMax, yMin, yMax):
	randX = getRandCoord(xMin, xMax);
	randY = getRandCoord(yMin, yMax);
	
	return circleF(randX) > randY;
#

goal = math.pi;

def doNaiveMonteCarlo(precision):
	areaEstimated = 0;
	tries = 0.0;
	successes = 0.0;

	while abs(areaEstimated - goal) > precision and tries < 100000:
		if doNaiveMonteCarloTest(0, 4, 0, 1):
			successes += 1;
		
		tries += 1;
		
		areaEstimated = 4 * (successes / tries);
	
	return [areaEstimated, tries];
#

def doMeanMonteCarlo(precision):
	areaEstimated = 0;
	tries = 0.0;
	sum = 0.0;
	
	while abs(areaEstimated - goal) > precision and tries < 100000:
		randX = getRandCoord(0, 4);
		
		sum += circleF(randX);
		tries += 1;
		
		areaEstimated = 4 * (sum / tries);
	
	return [areaEstimated, tries];
#

def getNaiveMonteCarloDeviation(tries):
	successes = 0.0;
	
	for i in range(tries):
		if doNaiveMonteCarloTest(0, 4, 0, 1):
			successes += 1;
	
	areaEstimated = 4 * (successes / tries);
	
	return abs(areaEstimated - goal);
#

def getMeanMonteCarloDeviation(tries):
	sum = 0.0;
	
	for i in range(tries):
		randX = getRandCoord(0, 4);
		
		sum += circleF(randX);
	
	areaEstimated = 4 * (sum / tries);
	
	return abs(areaEstimated - goal);
#

def isIn4DSphere4D(x, y, z, a):
	return math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2) + pow(a, 2)) < 1;
#

def doNaiveMonteCarloTest4D():
	randX = getRandCoord(0, 1);
	randY = getRandCoord(0, 1);
	randZ = getRandCoord(0, 1);
	randA = getRandCoord(0, 1);
	
	return isIn4DSphere4D(randX, randY, randZ, randA);
#

goal2 = pow(math.pi, 2) / 2.0;

def doNaiveMonteCarlo4D(precision):
	areaEstimated = 0;
	tries = 0.0;
	successes = 0.0;

	while abs(areaEstimated - goal2) > precision and tries < 1000000:
		if doNaiveMonteCarloTest4D():
			successes += 1;
		
		tries += 1;
		
		areaEstimated = 16 * (successes / tries);
	
	return [areaEstimated, tries];
#


minError = 0.001;


print("a)");

naiveMonteCarlo = doNaiveMonteCarlo(minError);

print("naive method:");
print("estimated area: " + str(naiveMonteCarlo[0]));
print("tries: " + str(naiveMonteCarlo[1]));

meanMonteCarlo = doMeanMonteCarlo(minError);

print(" ");
print("mean value method:");
print("estimated area: " + str(meanMonteCarlo[0]));
print("tries: " + str(meanMonteCarlo[1]));


xses = [];
naiveYses = [];
meanYses = [];

for i in range(1, 250):
	naiveDeviation = getNaiveMonteCarloDeviation(i * 10);
	meanDeviation = getMeanMonteCarloDeviation(i * 10);
	
	xses.append(i);
	naiveYses.append(naiveDeviation);
	meanYses.append(meanDeviation);


plt.plot(xses, naiveYses);
plt.plot(xses, meanYses);
plt.xlabel("tries");
plt.ylabel("deviation");
plt.show();


print(" ");
print("c)");

fourDSphere = doNaiveMonteCarlo4D(minError);
print("estimated area of 4D unit sphere: " + str(fourDSphere[0]));

total2DTries = 0.0;
total4DTries = 0.0;

runs = 250;

for i in range(runs):
	total2DTries += doNaiveMonteCarlo(minError)[1];
	total4DTries += doNaiveMonteCarlo4D(minError)[1];

avg2DTries = total2DTries / float(runs);
avg4DTries = total4DTries / float(runs);

print(" ");
print("average tries for 2d unit circle: " + str(avg2DTries));
print("average tries for 4d unit sphere: " + str(avg4DTries));




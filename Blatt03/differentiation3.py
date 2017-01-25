print("numerical differentiation 3 [Ex. 7.15]")


import matplotlib.pyplot as plt;
import differentiation1 as dif;



def sheepFunc10(t, yVector):
	return 10 * yVector[0] * (1 - yVector[1]);
#

def sheepFunc9(t, yVector):
	return 9 * yVector[0] * (1 - yVector[1]);
#

def sheepFunc12(t, yVector):
	return 12 * yVector[0] * (1 - yVector[1]);
#

def wolfsFunc(t, yVector):
	return yVector[1] * (yVector[0] - 1);
#


fses1 = [];
y0ses1 = [];

fses1.append(sheepFunc10);
fses1.append(wolfsFunc);
y0ses1.append(3);
y0ses1.append(1);

fses2 = [];
y0ses2 = [];

fses2.append(sheepFunc9);
fses2.append(wolfsFunc);
y0ses2.append(4);
y0ses2.append(2);

fses3 = [];
y0ses3 = [];

fses3.append(sheepFunc12);
fses3.append(wolfsFunc);
y0ses3.append(3);
y0ses3.append(2);


def testPredatorPrey(fses, y0ses):
	yVectorses = dif.rungeKuttaSystem(fses, 0, 5, y0ses, 0.05);
	
	xses = [];
	sheepYses = [];
	wolfsYses = [];
	
	x = 0;
	
	for yVector in yVectorses:
		sheepYses.append(yVector[0]);
		wolfsYses.append(yVector[1]);
		xses.append(x);
		x += 0.05;
	
	plt.plot(xses, sheepYses);
	plt.plot(xses, wolfsYses);
	plt.xlabel("x");
	plt.ylabel("y");
	plt.show();
#

testPredatorPrey(fses1, y0ses1);
testPredatorPrey(fses2, y0ses2);
testPredatorPrey(fses3, y0ses3);


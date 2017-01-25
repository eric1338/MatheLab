#print("numerical differentiation 1 [Ex. 7.13 a-b)]")

import math;


def odeSolver(f, a, b, y0, h, yp1Method):
	yses = [];
	
	x = a;
	y = y0;
	
	yses.append(y);
	
	while x <= b:
		y = yp1Method(f, x, y, h);
		
		yses.append(y);
		
		x += h;
	#
	
	return yses;
#

def eulerYP1(f, x, y, h):
	return y + h * f(x, y);
#

def heunYP1(f, x, y, h):
	k1 = h * f(x, y);
	k2 = h * f(x + h, y + k1);
	
	return y + 0.5 * (k1 + k2);
#

def rungeKuttaYP1(f, x, y, h):
	k1 = h * f(x, y);
	k2 = h * f(x + 0.5 * h, y + 0.5 * k1);
	k3 = h * f(x + 0.5 * h, y + 0.5 * k2);
	k4 = h * f(x + h, y + k3);
	
	return y + (1 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4);
#

def fkFunc(f, x, y, h, yp1Func, q, pk, step):
	if step == 1:
		fh = yp1Func(f, x, y, h);
		fqh = yp1Func(f, x, y, q * h);
	else:
		fh = fkFunc(f, x, y, h, yp1Func, q, pk, step - 1);
		fqh = fkFunc(f, x, y, q * h, yp1Func, q, pk, step - 1);
	
	return fh + ((fh - fqh) / (pow(q, pk) - 1.0));
#


def eulerYP1Richardson(f, x, y, h):
	return fkFunc(f, x, y, h, eulerYP1, 5, 23, 5);
#

def heunYP1Richardson(f, x, y, h):
	return fkFunc(f, x, y, h, heunYP1, 2, 13, 5);
#

def rungeKuttaYP1Richardson(f, x, y, h):
	return fkFunc(f, x, y, h, rungeKuttaYP1, 4, 18, 5);
#


def euler(f, a, b, y0, h):
	return odeSolver(f, a, b, y0, h, eulerYP1);
#

def heun(f, a, b, y0, h):
	return odeSolver(f, a, b, y0, h, heunYP1);
#

def rungeKutta(f, a, b, y0, h):
	return odeSolver(f, a, b, y0, h, rungeKuttaYP1);
#

def eulerRichardson(f, a, b, y0, h):
	return odeSolver(f, a, b, y0, h, eulerYP1Richardson);
#

def heunRichardson(f, a, b, y0, h):
	return odeSolver(f, a, b, y0, h, heunYP1Richardson);
#

def rungeKuttaRichardson(f, a, b, y0, h):
	return odeSolver(f, a, b, y0, h, rungeKuttaYP1Richardson);
#


def odeSystemSolver(fVector, a, b, y0Vector, h, yp1Methods):
	yVectorses = [];
	
	x = a;
	yVector = y0Vector;
	
	yVectorses.append(yVector);
	
	while x <= b:
		yp1Vector = yp1Methods(fVector, x, yVector, h);
		
		yVectorses.append(yp1Vector);
		
		yVector = yp1Vector;
		
		x += h;
	#
	
	return yVectorses;
#

def rungeKuttaYP1System(fVector, x, yVector, h):
	nF = len(fVector);
	
	k1Vector = [];
	yVectorPlusHalfK1Vector = [];
	
	for i in range(nF):
		k1El = h * fVector[i](x, yVector);
		k1Vector.append(k1El);
		yVectorPlusHalfK1Vector.append(yVector[i] + 0.5 * k1El);
	
	k2Vector = [];
	yVectorPlusHalfK2Vector = [];
	
	for i in range(nF):
		k2El = h * fVector[i](x + 0.5 * h, yVectorPlusHalfK1Vector);
		k2Vector.append(k2El);
		yVectorPlusHalfK2Vector.append(yVector[i] + 0.5 * k2El);
	
	k3Vector = [];
	yVectorPlusK3Vector = [];
	
	for i in range(nF):
		k3El = h * fVector[i](x + 0.5 * h, yVectorPlusHalfK2Vector);
		k3Vector.append(k3El);
		yVectorPlusK3Vector.append(yVector[i] + k3El);
	
	yp1Vector = [];
	
	for i in range(nF):
		k4El = h * fVector[i](x + h, yVectorPlusK3Vector);
		
		yp1 = yVector[i] + (1 / 6.0) * (k1Vector[i] + 2 * k2Vector[i] + 2 * k3Vector[i] + k4El);
		
		yp1Vector.append(yp1);
	
	return yp1Vector;
#

def rungeKuttaSystem(fVector, a, b, y0Vector, h):
	return odeSystemSolver(fVector, a, b, y0Vector, h, rungeKuttaYP1System);
#





# trueVals = [];

# for i in range(8): trueVals.append(exT(i / 10.0, 0));

# bestError = 9999;
# bestQ = -1;
# bestPK = -1;

# for i in range(2, 6):
	# for j in range(2, 25):
		# qFU = i;
		# pkFU = j;
	
		# fns = heunRichardson(exT, 0, 0.6, 1, 0.1);
		
		# error = 0;
		
		# for k in range(8):
			# error += abs(trueVals[k] - fns[k]);
		
		# if (error < bestError):
			# bestError = error;
			# bestQ = qFU;
			# bestPK = pkFU;
# #

# print(bestQ);
# print(bestPK);

# qFU = bestQ;
# qPK = bestPK;

# print(trueVals);
# print(heunRichardson(exT, 0, 0.6, 1, 0.1));


print("numerical differentiation 4 [Ex. 7.16]")


import math;
import matplotlib.pyplot as plt;
import differentiation1 as dif;


def myF(x, y):
	return x * math.sin(x * y);
#


xses = [];

for i in range(201): xses.append(i / 10.0);

yses = dif.rungeKutta(myF, 0, 20, 1, 0.1);


plt.plot(xses, yses);
plt.xlabel("x");
plt.ylabel("y");
plt.show();


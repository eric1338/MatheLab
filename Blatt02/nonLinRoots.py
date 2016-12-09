print("roots [Ex. 4.8 a-f)]")

import math;
import matplotlib.pyplot as plt;

print("a)");

xses = [];
fLeft = [];
fRight = [];

for i in range(200):
	x = (i / 100.0) - 1;
	
	xses.append(x);
	fLeft.append(0.5 * pow(math.e, -pow(x, 2)));
	fRight.append(x);


plt.plot(xses, fLeft);
plt.plot(xses, fRight);
plt.xlabel('x');
plt.ylabel('y');
plt.show();


print("fibonacci [Ex. 2.3 c+d)]")

import time;
import matplotlib.pyplot as plt;

print("c)");

def fibonacciFunc(x):
	if x <= 1: return 1;
	
	return fibonacciFunc(x - 1) + fibonacciFunc(x - 2);


results = [];

for i in range(20):
	fib = fibonacciFunc(i);
	print("fib(" + str(i + 1) + "): " + str(fib));
	results.append(fib);
	

print(" ");
print("d)");

runtimes = [];

for i in range(30):
	timeStart = time.time();
	fibonacciFunc(i);
	ms = 1000 * (time.time() - timeStart);
	runtimes.append(ms);


plt.plot(runtimes);
plt.xlabel('x');
plt.ylabel('runtime fib(x) [ms]');
plt.show();

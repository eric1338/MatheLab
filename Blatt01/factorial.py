print("factorial [Ex. 2.3 a+b)]")

import math;
import scipy.integrate as itg;

print("a)");

n = int(input("n = "));

factorialIterative = 1;

for i in range(n):
    factorialIterative *= (i + 1);


print("iterative result: " + str(factorialIterative));


def factorialFunc(x):
    if x <= 0: return 1;
	
    return x * factorialFunc(x - 1);


factorialRecursive = factorialFunc(n);

print("recursive result: " + str(factorialRecursive));

print(" ");
print("b)");

def bFunc(t, z):
	return math.pow(math.log(1 / t), z - 1);


for i in range(1, 10):
	factorialResult = factorialFunc(i - 1);
	integrateResult = itg.quad(lambda x: bFunc(x, i), 0, 1);
	
	print("n = " + str(i));
	print("(n - 1)! = " + str(factorialResult));
	print("Gamma(n) = " + str(integrateResult));
	print(" ");


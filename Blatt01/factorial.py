print("factorial [Ex. 2.3 a)]")

n = int(input("n="));

factorialIterative = 1

for i in range(n):
    factorialIterative *= (i + 1)


print("iterative result: " + str(factorialIterative))


def factorialFunc(x):
    if x <= 0: return 1
	
    return x * factorialFunc(x - 1)



factorialRecursive = factorialFunc(n)

print("recursive result: " + str(factorialRecursive))
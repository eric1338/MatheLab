print("bucket [Ex. 2.5 a-e)]")

import math;

class Bucket:
	poison = 1;
	cleaningIterations = 0;
	waterUsed = 0;
	
	def __init__(self, alpha, beta, eps):
		self.alpha = alpha;
		self.beta = beta;
		self.eps = eps;
	
	def doOneClean(self):
		water = self.beta - self.alpha;
		self.waterUsed += water;
		
		#self.poison = (1 - water) * self.poison;
		self.poison = (self.alpha / float(self.beta)) * self.poison;
	
	
	def clean(self):
		while (self.poison >= self.eps):
			self.cleaningIterations += 1;
			self.doOneClean();
	


bu = Bucket(0.01, 0.15, 10e-9);
bu.clean();

print("a)");

print("number of iterations: " + str(bu.cleaningIterations));

print(" ");
print("b)");

print("water used: " + str(bu.waterUsed) + " * v");
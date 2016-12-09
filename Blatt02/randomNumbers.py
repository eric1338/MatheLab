print("random [Ex. 3.6 a-e)]")

import math;


class RNG:
	a = 0;
	b = 0;
	m = 0;
	x = 0;
	bits = [];
	
	def __init__(self, pA = 7141, pB = 54773, pM = 259200):
		self.x = 1;
		self.a = pA;
		self.b = pB;
		self.m = pM;
	
	
	def printParameters(self):
		print("a = " + str(self.a) + ", b = " + str(self.b) + ", m = " + str(self.m));
	
	
	def getRandomNumber(self):
		self.x = (self.a * self.x + self.b) % self.m;
		return self.x;
	
	
	def addNumbers(self, number):
		binNumber = bin(number)[2:];
		
		for bitNumber in binNumber:
			self.bits.append(int(bitNumber));
	
	
	def fillNumbers(self, iterations):
		for i in range(iterations):
			self.addNumbers(self.getRandomNumber());
	
	
	def makeSymmetryTest(self):
		sum = 0;
		
		for b in self.bits:
			sum += b;
		
		deviation = abs(0.5 - (sum / float(len(self.bits))));
		
		print("symmetry test:")
		print("deviation = " + str(deviation));
	
	
	def applyNeumannFilter(self):
		tempBits = self.bits;
		self.bits = [];
		
		nIterations = int(math.floor(len(tempBits) / 2.0));
		
		for i in range(nIterations):
			bit1 = tempBits[i * 2];
			bit2 = tempBits[i * 2 + 1];
			
			if (bit1 == 0 and bit2 == 1):
				self.bits.append(0);
			elif (bit1 == 1 and bit2 == 0):
				self.bits.append(1);




print("b)");

rng = RNG();
rng.fillNumbers(1000);
rng.makeSymmetryTest();

print(" ");
print("c)");
rng.applyNeumannFilter();
rng.makeSymmetryTest();

print(" ");
print("d)");

rng1 = RNG(100, 1000, 10000);
rng1.printParameters();

rng1.fillNumbers(1000);
rng1.makeSymmetryTest();

rng2 = RNG(1000, 10000, 100000);
rng2.printParameters();

rng2.fillNumbers(1000);
rng2.makeSymmetryTest();


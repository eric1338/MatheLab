print("random [Ex. 3.6 a-d)]")

import math;


class RNG:
	#a = 0;
	#b = 0;
	#m = 0;
	#x = 0;
	#bits = [];
	
	def __init__(self, pA = 7141, pB = 54773, pM = 259200):
		self.bits = [];
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
	
	
	def isPeriod(self, periodLength):
		nBits = len(self.bits);
		
		if periodLength * 2 > nBits: return False;
		
		iterations = int(math.floor(nBits / float(periodLength)));
		
		for i in range(periodLength):
			compareElement = self.bits[i];
		
			for j in range(1, iterations):
				key = j * periodLength + i;
				
				if key >= nBits: break;
				
				element = self.bits[key];
				
				if element != compareElement:
					return False;
		
		return True;
	
	
	def makePeriodicityTest(self):
		periodLength = -1;
		
		maximumPeriod = self.m * int(math.ceil(math.log(self.m, 2)));
		
		if maximumPeriod > 100002: maximumPeriod = 100002;
		
		for i in range(1, maximumPeriod):
			if i > 100000:
				periodLength = -2;
				break;
			
			if self.isPeriod(i):
				periodLength = i;
				break;
		
		print("periodicty test:");
		
		if periodLength < -1.5:
			print("no period shorter than 100,000 found.");
		elif periodLength < -0.5:
			print("no period found.");
		else:
			print("period length = " + str(periodLength));

	
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
rng.fillNumbers(25000);
rng.makeSymmetryTest();
print(" ");
rng.makePeriodicityTest();


print(" ");
print("c)");
rng.fillNumbers(75000);
rng.applyNeumannFilter();
rng.makeSymmetryTest();
print(" ");
rng.makePeriodicityTest();

print(" ");
print("d)");

rng1 = RNG(1, 1, 10);
rng1.printParameters();

rng1.fillNumbers(25000);
print(len(rng1.bits));
rng1.makeSymmetryTest();


print(" ");

rng2 = RNG(20, 30, 100000);
rng2.printParameters();

rng2.fillNumbers(25000);
rng2.makeSymmetryTest();

print(" ");

rng3 = RNG(214013, 2531011, pow(2, 32));
rng3.printParameters();

rng3.fillNumbers(25000);
rng3.makeSymmetryTest();



import math

class Vector(object):
	def __init__(self, data):
		self.data = data
	
	def __repr__(self):
		return self.__class__.__name__+'('+repr(self.data)+')'
	
	def __add__(self, other):
		return self.__class__([a + b for a, b in zip(self.data, other.data)])
	
	def __sub__(self, other):
		return self.__class__([a - b for a, b in zip(self.data, other.data)])
	
	# use zip() for the last two operators
	def __mul__(self, other):
		a = []
		for i in range(len(self.data)):
			a.append(self.data[i] * other)
		return self.__class__(a)

	def __truediv__(self, other):
		a = []
		#the loop in __truediv__ can be rewritten as:
		#for d in self.data:
		#	a.append(d / other)
		for i in range(len(self.data)):
			a.append(self.data[i] / other)
		return self.__class__(a)

	# @property
	def len(self):
		vecsum = 0
		for i in self.data:
			vecsum += math.pow(i, 2)
			magnitude = math.sqrt(vecsum)
		self.data = float(magnitude)
		return self.data
	
	@property
	def unit(self):
		vecsum = 0
		unitvec = []
		for i in self.data:
			vecsum += math.pow(i, 2)
		veclen = math.sqrt(vecsum)
		for i in self.data:
			unitvec.append(i / veclen)
		return self.__class__(unitvec)

	#@property
	def dot(self, other):
		return (sum((a * b) for a, b in zip(self.data, other.data)))
	
	def cross(self, other):

		c_x = self.data[1]*other.data[2] - self.data[2] * other.data[1]
		c_y = self.data[2]*other.data[0] - self.data[0] * other.data[2]
		c_z = self.data[0]*other.data[1] - self.data[1] * other.data[0]
		
		vector_product = [c_x, c_y, c_z]
		
		return self.__class__(vector_product) #print(f'Testing to see it it works, first: {self.data} and second: {other.data}')
	
	def lerp(self, other, t):
		lerpvec = (other - self) * t + self
		return self.__class__(lerpvec)

class Matrix(object):
	def __init__(self, data):
		self.data = data
		
	def __repr__(self):
		return self.__class__.__name__+'('+repr(self.data)+')'

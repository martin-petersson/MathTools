import math

class baseClass:
	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return self.__class__.__name__+'('+repr(self.data)+')'

class Vector(baseClass):
	def __add__(self, other):
		return self.__class__([a + b for a, b in zip(self.data, other.data)])
	
	def __sub__(self, other):
		return self.__class__([a - b for a, b in zip(self.data, other.data)])
	
	def __mul__(self, other):
		a = []
		for i in self.data:
			a.append(i * other)
		return self.__class__(a)

	def __truediv__(self, other):
		a = []
		for i in self.data:
			a.append(i / other)
		return self.__class__(a)

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

	def dot(self, other):
		return (sum((a * b) for a, b in zip(self.data, other.data)))
	
	# extend cross product to R^7
	def cross(self, other):
		c_x = self.data[1]*other.data[2] - self.data[2] * other.data[1]
		c_y = self.data[2]*other.data[0] - self.data[0] * other.data[2]
		c_z = self.data[0]*other.data[1] - self.data[1] * other.data[0]
		vector_product = [c_x, c_y, c_z]
		return self.__class__(vector_product)
	
	def lerp(self, other, t):
		lerpvec = (other - self) * t + self
		return self.__class__(lerpvec)

class Matrix(baseClass):
	
	# matrix times vector
	def __mul__(self, other):
		vecbuffer = []
		vecresult = []

		for vecrow in self.data:
			for element in range(len(vecrow)):
				mulmatvec = vecrow[element] * other.data[element]
				vecbuffer.append(mulmatvec)
			vecsum = sum(vecbuffer)
			vecresult.append(vecsum)
			vecbuffer = []
		return Vector(vecresult)

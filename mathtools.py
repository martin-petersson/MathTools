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

"""
def polynomial(arguments):

	for element in arguments:
		print('can take a vector or a list/tuple')

def solve_right_triangle(a, b, c):
	return
"""

"""
def sphericalcoord(r, theta, phi): # altitude, longitude, latitude
	x = r * math.sin(theta) * math.cos(phi)
	y = r * math.sin(theta) * math.sin(phi)
	z = r * math.cos(theta)
	return sphere_x, sphere_y, sphere_z

def cartesian_to_spherical(x, y, z): # z is up
	r = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))
	theta = math.acos(z / r)
	phi = math.atan(y / x)
	return r, theta, phi
"""

"""
	def pointdistance(x, y):
		return math.sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
	
	# get angle between two vectors
	def vecangle(x, y): # this is unfished fix it
		zerovector = []
		for i in range(len(x)):
			zerovector.append(0)
		# put both vectors at origo
		xorigo = vecadd(vecsub(zerovector, x), x)
		yorigo = vecadd(vecsub(zerovector, y), y)
		dotxy = dotproduct(x, y)
		dotlen = veclen(x) * veclen(y)
		return math.acos(dotxy / dotlen)
	
	def barycentric(x, y, z, a, b, c):
		inside = a + b + c
		return vecdiv(vecadd(vecadd(vecmul(x, a), vecmul(y, b)), vecmul(z, c)), inside)
	
	# loop through list
	def feature_rescaling(x):
		xmin = x[0]
		xmax = x[0]
		newvec = []
		for i in x: # get xmin
			if i < xmin:
				xmin = i
			if i > xmax: # get xmax
				xmax = i
		for g in x:
			r = (g - xmin) / (xmax - xmin)
			#print('feature rescaling:', r)
			newvec.append(r)
		return newvec
	
	def vecmean(x): # mean of vectors not components
		zerovec = []
		meanvec = []
		for i in x[0]:
			zerovec.append(0)
		for i in x:
			zerovec = vecadd(i, zerovec)
		for i in zerovec:
			mean = i / len(x)
			meanvec.append(mean)
		return meanvec

def spherical_to_cartesian(r, theta, phi): # altitude, longitude, latitude
	x = r * math.sin(theta) * math.cos(phi)
	y = r * math.sin(theta) * math.sin(phi)
	z = r * math.cos(theta)
	return sphere_x, sphere_y, sphere_z

def cartesian_to_spherical(x, y, z): # z is up
	r = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))
	theta = math.acos(z / r)
	phi = math.atan(y / x)
	return r, theta, phi

def parabola(x, h, k):
	return a * math.pow(x - h, 2) + k

def cubicpolynomial(x, a, b, c):
	return math.pow(x, 3) + (a * math.pow(x, 2)) + (b * x) + c
"""

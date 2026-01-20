import math

class baseClass:
	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return self.__class__.__name__+'('+repr(self.data)+')'

	# vector and matrix addition
	def __add__(self, other):
		match (self, other):
			case (Vector(), Vector()):
				return self.__class__([a + b for a, b in zip(self.data, other.data)])
			case (Matrix(), Matrix()):
				matrixsum = []
				mrow = []
				for n in range(len(self.data)):
					for m in range(len(self.data[0])):
						mrow.append(self.data[n][m] + other.data[n][m])
					matrixsum.append(mrow)
					mrow = []
				return self.__class__(matrixsum)
			case (Matrix(), Vector()):
				matrixsum = []
				mrow = []
				for n in range(len(self.data)):
					for m in range(len(self.data[0])):
						mrow.append(self.data[n][m]+ other.data[m])
					matrixsum.append(mrow)
					mrow = []
				return self.__class__(matrixsum)
			case (Vector(), Matrix()):
				matrixsum = []
				mrow = []
				for n in range(len(other.data)):
					for m in range(len(other.data[0])):
						mrow.append(other.data[n][m]+ self.data[m])
					matrixsum.append(mrow)
					mrow = []
				return self.__class__(matrixsum)

	def __matmul__(self, other):
		match (self, other):
			# matrix times vector
			case (Matrix(), Vector()):
				product = []
				matbuffer = []
				for m in self.data:
					for i in range(len(m)):
						matmul = m[i] * other.data[i]
						matbuffer.append(matmul)
					vecsum = sum(matbuffer)
					product.append(vecsum)
					matbuffer = []
				return Vector(product)

			case (Vector(), Matrix()):
				raise ValueError('Must use row property or 1xn matrix')
				
			# matrix times matrix
			case (Matrix(), Matrix()):
				if (len(self.data[0]) == len(other.data)):
					product = []
					rowproduct = []
					matbuffer = 0
					for mrow in self.data:
						for nrow in range(len(other.data[0])):
							for ncol in range(len(other.data)):
								matrow = mrow[ncol]
								nmatrow = other.data[ncol]
								nmatcol = nmatrow[nrow]
								matbuffer += matrow * nmatcol
							rowproduct.append(matbuffer)
							matbuffer = 0
						product.append(rowproduct)
						rowproduct = []
					return self.__class__(product)
				else:
					raise ValueError('Matrices need to be of equal size or mxn and nxp')


class Vector(baseClass):
	@property
	def x(self):
		return self.data[0]

	@x.setter
	def x(self, value):
		self.data[0] = value

	@property
	def y(self):
		return self.data[1]

	@y.setter
	def y(self, value):
		self.data[1] = value

	@property
	def z(self):
		return self.data[2]

	@z.setter
	def z(self, value):
		self.data[2] = value

	@property
	def w(self):
		return self.data[3]

	@w.setter
	def w(self, value):
		self.data[3] = value
	
	# subtraction
	def __sub__(self, other):
		return self.__class__([a - b for a, b in zip(self.data, other.data)])

	# multiplication
	def __mul__(self, other):
		match (self, other):
			case (Vector(), int() | float()) | (int() | float(), Vector()):
				print("vafan gör vi här?")
				a = []
				for i in self.data:
					a.append(i * other)
				return self.__class__(a)

	# division
	def __truediv__(self, other):
		a = []
		for i in self.data:
			a.append(i / other)
		return self.__class__(a)

	# vector length
	@property
	def len(self):
		vecsum = 0
		for i in self.data:
			vecsum += i**2
		length = float(math.sqrt(vecsum))
		return length
	
	# Euclidean distance
	def distance(self, other):
		match (self, other):
			case (Vector(), Vector()):
				if len(self.data) == len(other.data):
					vecdiff = self - other
					distance = vecdiff.len
				else:
					raise ValueError('Vectors have to be the same number of components')
			case (Vector(), Matrix()):
				raise ValueError('Euclidean distance only works between two vectors')	
		return distance

	# normalize vector
	@property
	def unit(self):
		vecsum = 0
		unitvec = []
		veclen = self.len
		if veclen == 0:
			raise ValueError('Cannot unitize a zero-vector')
		for i in self.data:
			unitvec.append(i / veclen)
		return self.__class__(unitvec)

	# dot product
	def dot(self, other):
		return (sum((a * b) for a, b in zip(self.data, other.data)))
	
	# cross product
	def cross(self, other):
		c_x = self.data[1]*other.data[2] - self.data[2] * other.data[1]
		c_y = self.data[2]*other.data[0] - self.data[0] * other.data[2]
		c_z = self.data[0]*other.data[1] - self.data[1] * other.data[0]
		vector_product = [c_x, c_y, c_z]
		return self.__class__(vector_product)
	
	# linear interpolation
	def lerp(self, other, t):
		lerpvec = (other - self) * t + self
		return self.__class__(lerpvec)
	
	# row vector
	@property
	def row(self):
		return Matrix([self.data])

	# column vector
	@property
	def col(self):
		m = []
		n = []
		for c in self.data:
			n = []
			n.append(c)
			m.append(n)
		return Matrix(m)


class Matrix(baseClass):
	# matrix subtraction
	def __sub__(self, other):
		matrixdiff = []
		mrow = []
		for n in range(len(self.data)):
			for m in range(len(self.data[0])):
				mrow.append(self.data[n][m] - other.data[n][m])
			matrixdiff.append(mrow)
			mrow = []
		return self.__class__(matrixdiff)

	def __mul__(self, other):
		match (self, other):
			# matrix times scalar
			case (Matrix(), float() | int()):
				product = []
				mrow = []

				for n in self.data:
					mrow = []
					for m in n:
						mrow.append(m * other)
					product.append(mrow)

				return self.__class__(product)
			# hadamard product of two matrices
			case (Matrix(), Matrix()):
				product = []
				mrow = []
				for n in range(len(self.data)):
					mrow = []
					for m in range(len(self.data[0])):
						mrow.append(self.data[n][m] * other.data[n][m])
					product.append(mrow)
				return self.__class__(product)

			case (Matrix(), Vector()):
				raise ValueError('Hadamard product requires matrices to be of the same size')

	# return identity matrix of size n
	def identity(n):
		identity = []
		mrow = []
		diagonal = 0
		for m in range(n):
			for i in range(n):
				if diagonal == i:
					mrow.append(1)
				else:
					mrow.append(0)
			diagonal += 1
			identity.append(mrow)
			mrow = []
		return Matrix(identity)

	# matrix size
	@property
	def size(self):
		m = len(self.data)
		n = len(self.data[0])
		return (m, n)

	# matrix transpose
	@property
	def transpose(self):
		transpose = []
		n = []
		for c in range(len(self.data[0])):
			n = []
			for r in range(len(self.data)):
				mrow = self.data[r]
				crow = mrow[c]
				n.append(crow)
			transpose.append(n)
		return self.__class__(transpose)

	# Create Vector() from vector with row or col property
	@property
	def to_vector(self):
		if (self.size[0] == 1) and (self.size[1] > 1):
			return Vector(self.data[0])
		if (self.size[0] > 1) and (self.size[1] == 1):
			vector = []
			for i in self.data:
				vector.append(i[0])
			return Vector(vector)
		if (self.size[0] > 1) and (self.size[1] > 1):
			raise ValueError('Matrix required to be of size 1xn or nx1')

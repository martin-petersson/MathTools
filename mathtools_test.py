from mathtools import Vector
import math

def test_vector_length():
	assert Vector([1, 1]).len == math.sqrt(2) # = 1.4142135623730951

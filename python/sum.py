def sum(a, b):
	if(b != 0):
		s = (a ^ b)
		c = (a & b) << 1
		return sum(s, c)
	else:
		return a

def recursive_sum(a, b):
	if(b != 0):
		s = (a ^ b)
		c = (a & b) << 1
		return sum(s, c)
	else:
		return a


def iterative_sum(a, b):
	while(b != 0):
		s = (a ^ b)
		b = (a & b) << 1
		a = s
	return a

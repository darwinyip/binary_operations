def sum(a, b):
	return (a ^ b) ^ ((a & b) << 1)

int recursive_sum(int a, int b) {
	if(b != 0) {
		int s = (a ^ b);
		int c = (a & b) << 1;
		return recursive_sum(s, c);
	}
	else return a;
}

int iterative_sum(int a, int b) {
	int s;
	while(b != 0) {
		s = (a ^ b);
		b = (a & b) << 1;
		a = s;
	}
	return a;
}

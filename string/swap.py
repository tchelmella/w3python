def swapstr(a,b):
	s1 = b[:2] + a[2:]
	s2 = a[:2] + b[2:]

	return s1 + ' ' + s2

print(swapstr('abc','xyz'))

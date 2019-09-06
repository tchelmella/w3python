def celc(f):
	c = ((f-32) * 5/9)
	return c

def fahr(c):
	f = ((c - 32) * 5 / 9)
	return f

print(celc(60))
print(fahr(45))
print(celc(75))
print(fahr(80))

n = range(1,76)
c1 = 0
c2 = 0
for i in n:
	if i%2 == 0:
		c1 += 1
	else:
		c2 += 1

print("Number of even numbers : " , c1)
print("Number of odd numbers : " , c2)

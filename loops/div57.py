count = 0
x = []
for i in range(1499,2701):
	if i % 7 == 0 and i % 5 == 0:
		x.append(str(i))
		count = count + 1
print(x)
print(count)

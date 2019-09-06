def remnth(data,n):
	part1 = data[:n]
	part2 = data[n+1:]
	return part1 + part2

print(remnth('Python',0))
print(remnth('Python',1))
print(remnth('Python',2))

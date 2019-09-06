data = int(input("Enter the list of numbers"))

count = 0

for i in range(len(data)):
	count = i + 3
	print(count)
	if count == i:
		print(data[i])

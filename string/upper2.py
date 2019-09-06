def upper2(data):
	count = 0
	for i in data[0:4]:
		if i.upper() == i:
			count += 1
	if count >=2:
		return data.upper()
	return data

print(upper2('Python'))
print(upper2('PYthon'))
print(upper2('PyTHon'))


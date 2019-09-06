import string

#data = 'w3resource'

def strlen2(data):
	if len(data) < 2:
		return data
	if len(data) == 2:
		return data*2
	else:
		return (data[0:2] + data[-2:])

print(strlen2('w3resource'))
print(strlen2('w3'))
print(strlen2('w'))

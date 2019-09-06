import string

data = 'Hi, you have a package coming today.'

print(len(data))

def stringlen(str1):
	count = 0
	for i in str1:
		count += 1

	return count

print(stringlen('Hi, you have a package coming today.'))

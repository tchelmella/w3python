import string

def adding(data):
	if len(data) < 3:
		return 'Length of the string should be more than three'
	elif data[-3:] == 'ing':
		return data + 'ly'
	else:
		return data + 'ing'

print(adding('abc'))
print(adding('string'))
print(adding('ca'))

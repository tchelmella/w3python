import string

def occur(data):
	count = 0
	val = data[0]
	for i in data:
		if val in data:
			data = data.replace(val,'$')
			data = val + data[1:]

	return data

print(occur('restart'))
print(occur('tomato'))

'''
def oddindex(data):
	count = ""
	for i in range(len(data)):
		if i%2==0:
			count += data[i]
	return count
'''

def oddindex(data):
	return data[0::2]

print(oddindex('abcdef'))
print(oddindex('python'))

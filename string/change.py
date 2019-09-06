def change(data):
	first = data[0]
	last = data[-1]
	final = last + data[1:len(data)-1] + first
	return final

print(change('Python'))
print(change('condition'))
print(change('shirt'))
print(change('abcd'))
print(change('12345'))

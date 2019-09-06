def rev(data):
	if len(data) % 4 == 0:
		#return ''.join(reversed(data))
		return data[::-1]

print(rev('string'))
print(rev('condition'))
print(rev('tangents'))
print(rev('Tulsidas'))
print(rev('Nemethos'))
print(rev('Paytonos'))

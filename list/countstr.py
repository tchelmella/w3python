a = ['abc', 'xyz', 'aba', '1221']

def countstr(list):
	count = 0
	for i in list:
		if len(i) < 2:
			return i
		elif i[0] == i[-1]:
			count += 1
	return count

print(countstr(a))

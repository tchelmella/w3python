a = [1,2,3,3,4,5,5,5,6]

def remdups(list):
	dups = set()
	list1 = []
	for i in list:
		if i not in dups:
			list1.append(i)
			dups.add(i)
	return dups
print(remdups(a))

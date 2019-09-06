import operator

a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def sortuple(list):
	return sorted(list,key=operator.itemgetter(1))

print(sortuple(a))

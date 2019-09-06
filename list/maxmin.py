a = [12,54,2,5]

print(max(a))
print(min(a))

def maxmin(list):
	max = list[0]
	for a in list:
		if a > max:
			max = a
	return max

print(maxmin(a))

def minmax(list):
	min = list[0]
	for a in list:
		if a < min:
			min = a
	return min

print(minmax(a))

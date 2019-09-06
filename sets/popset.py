def popset(set1):
	found = False
	val = input("Enter the item to fnd")
	for i in set1:
		if (i == val):
			found = True

	if found == True:
		set1.discard(val)
		return set1
	else:
		print("Item not found")

print(popset({1,2,3,4,5}))
print(popset({"Red","Green","Orange","Blue"}))

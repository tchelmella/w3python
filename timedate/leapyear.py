def leap_year(y):
	if y % 400 == 0:
		return True
	if y % 100 == 0:
		return False
	if y % 4 == 0:
		return True
	else:
		return False

print(leap_year(1900))
print(leap_year(2004))

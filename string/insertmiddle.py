def middle(str,data):
	ind = int(len(data)/2)
	return str[:ind] + data + str[ind:]

print(middle('[[[]]]','Python'))
print(middle('<<<>>>','1234'))
print(middle('{{}}}','join'))

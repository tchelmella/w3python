import string

name = input("Enter the string")
str1 = ""
for i in name:
	str1 = i + str1

print(str1)

print(name[::-1])

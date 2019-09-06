def addtags(i,data):
	return "<%s>%s<%s>" % (i,data,i)

print(addtags('p','This is a paragraph'))
print(addtags('b','This is a bold line'))

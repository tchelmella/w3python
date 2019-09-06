import string
'''
def charfreq(data):
	dict = {}
	for i in data:
		keys = dict.keys()
		if i in keys:
			dict[i] += 1
		else:
			dict[i] = 1
	return dict
'''

'''
def charfreq(data):
	return{x:string.count(x) for x in data}
'''

charfreq = lambda string: {x:string.count(x) for x in string}
print(charfreq('www.google.com'))


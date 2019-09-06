'''
def longest(data):
	word = []
	for i in data:
		word.append((len(i),i))
	word.sort()
	return word[-1][1]
'''

def longest(data):
	word = sorted(data,reverse=True,key=len)
	return word[0]

print(longest(["hope","you","great","weekend"]))


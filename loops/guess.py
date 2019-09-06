import random

target, guess = random.randint(1,10),0

while target != guess:
	guess = int(input("Guess a number between 1 and 10 until you get it right:"))
	print(target)

print('Well guessed')

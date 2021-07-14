import random

number=random.randrange(1,10)

guess=0

count=0

while guess !=number :
	guess = int(guess)
	count += 1
if guess < number:
        print("You've guessed too low!")
elif guess > number:
        print("You've guessed too high!") 
	
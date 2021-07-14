
import random

number = random.randrange(1, 10)
guess = 0
count = 0

while guess != number:
    guess = input("Please guess a number between 1 and 9. When you want to end the game print 'exit': ")

    
    guess = int(guess)
    count += 1
    if guess not in range(1, 10):
        print("You have to guess a number between 1 and 9!")
    elif guess < number:
        print("You've guessed too low!")
    elif guess > number:
        print("You've guessed too high!") 
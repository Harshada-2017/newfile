import random

number = random.randint(1, 20)

guess = int(input("Guess a number (1-20): "))

if guess == number:
    print("Correct!")
else:
    print("Wrong! The number was", number)
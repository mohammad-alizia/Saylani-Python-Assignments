import random

num = random.randint(1,30)
guesses = 0

while guesses < 3:
    guess = int(input("Take a guess: "))
    guesses = guesses + 1

    if guess < num:
        print("Think of a greater number")

    elif guess > num:
        print("Think of a smaller number")

    elif guess == num:
        print("You guessed it right!")
        break



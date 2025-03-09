import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
print("If you want to exit the game, please enter 0")
guess = 0

while guess != answer:
    guess = int(input())

    if guess == 0:
        print("You have entered 0, that will exit the game")
        break  

    if guess != answer:
        if answer < guess:
            print("Please guess lower.")
        else:
            print("Please guess higher.")

    if guess == answer:
        print("Well done, you guessed it!")



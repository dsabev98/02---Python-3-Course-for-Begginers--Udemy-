answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("Well done, you guessed it!")    
else:
    if guess != answer:
        if answer < guess:
            print("Please guess lower.")
        else:
            print("Please guess higher.")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it!")
        else:
            print("Sorry, you have not guessed correctly.")
    


# if guess < answer:
#     print("Please guess higher.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
# elif guess > answer:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
# else:
#     print("Well done, you guessed it!")


# for _ in iter(int, 1):  # Infinite loop
#     guess = int(input())
#     if guess < answer:
#         print("Please guess higher.")
#     elif guess > answer:
#         print("Please guess lower.")
#     else:
#         print("Well done, you guessed it!")
#         break

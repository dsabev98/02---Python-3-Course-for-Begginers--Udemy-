name = str(input("What is your name? "))
age = int(input("What is your age? "))

if 18 <= age < 31:
    print(f"Welcome to the holiday, {name}")
else:
    print("I'm sorry, our holidays are only for cool people")
for i in range(1, 13):
    print("No. {:2} squared is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3 ))
    print("*" * 80)

name = "Mitko"
age = 15
print(age)
print(i)

is_prime = True

if is_prime == True:
    print("You are old enough to vode")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vode")
    print("Please put an X in the box")

is_prime = True
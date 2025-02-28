#         43210987654321
#         01234567890123
# parrot = "Norwegian Blue"

# print(parrot)
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

# print()

# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

# print(parrot[3:5])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

# print(parrot[0:6])    # Norweg
# print(parrot[3:5])    # we
# print(parrot[0:9])    # Norwegian
# print(parrot[:9])     # Norwegian
# print(parrot[10:14])  # Blue
# print(len(parrot))

# letters = "abcdefghijklmnopqrstuvwxyz"
number = "9,223;372:036 854,775;807"

separators =  ""

for char in number: 
    if not char.isnumeric():
        separators += char

# print(separators)

values = "".join(char if char not in separators else " " for char in number).split()

print(sum([int(val) for val in values]))


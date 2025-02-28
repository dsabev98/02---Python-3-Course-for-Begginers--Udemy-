# This string contains newline characters (\n) which will split the string over several lines
split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

# This string contains tab characters (\t) which will insert tab spaces between the numbers
tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

# This prints a string that includes both single and double quotes using escape characters (\')
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# This prints the same string using escape characters (\") for double quotes
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

# This prints the same string using triple quotes (""") and a backslash (\) to escape the newline
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")

# This string uses triple quotes and a backslash (\) to escape the newline, splitting the string over several lines
another_split_string = """This sting has been \
split over \
several \
lines"""

print(another_split_string)
# This prints a file path with escaped backslashes (\\)
print("C:\\Users\\tibuchalka\\notes.txt")

# This prints the same file path using a raw string (r) to avoid escaping backslashes
print(r"C:\Users\tibuchalka\notes.txt")



print("Today is a good day to learn Python")
print('Python is fun')
print("Pythons's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")

greetings = "Hello" 
name = "Mitko"
age = 24

print(greetings + name)

print(greetings + ' ' + name)

print(type(greetings))
print(type(age))

age_in_words = "2 years"

print(age)        # 2 years
print(type(age))    # <class 'str'>
print(name + f" is {age}" + " years old")

print(f"Pi is approximately {22 / 7:12.50f}")

pi = 22 / 7

print(f"Pi is approximately {pi:70.50f}")
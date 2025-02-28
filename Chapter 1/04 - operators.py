a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division    

print()

print(a + b / 3 - 4 * 12)   # 12 + 1 - 48 = -35
print(a + (b / 3) - (4 * 12))   # 12 + 1 - 48 = -35
print((((a + b) / 3) - 4) * 12)   # ((15 / 3) - 4) * 12 = 12
print(((a + b) / 3 - 4) * 12)   # ((15 / 3) - 4) * 12 = 12

C = a + b
D = C / 3
E = D - 4
print(E * 12)   # 12

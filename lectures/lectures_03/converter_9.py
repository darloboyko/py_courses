a = int(input ("Enter a  "))
b = int(input ("Enter b  "))
print(a, b)

c = a
a = b
b = c
print(a, b)

a = a + b
b = a - b
a = a - b
print(a, b)

a, b = b, a
print(a, b)


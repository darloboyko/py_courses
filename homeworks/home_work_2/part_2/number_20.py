from math import*

x = float(input("Enter x:  "))

print(round((pow(((log(x))**2), 1/3) + tan((cos(pi*x))))*(abs(log(x/10.5)+1/3)), 3))
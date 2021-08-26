from math import*

x = float(input("Enter x:  "))

print(round((sqrt(sin(x/2)**3)+pow((exp(1.3*x)+exp(-1.3*x)), 1/3))*(1/(abs(x+5/2))), 3))
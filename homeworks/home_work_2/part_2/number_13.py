from math import*

x = float(input("Enter x:  "))

print(round((pow((exp(-2 + x)), 1/5)*(1/(sqrt(x**2 + x**4 + (log(abs(x - 3.14))))))), 3))
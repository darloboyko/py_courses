from math import*

x = float(input("Enter x:  "))

print(round((abs(x*log(x)-4)*sqrt(x))*(1/(pow((exp(4*x-1)), 1/5))), 3))
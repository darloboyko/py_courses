#Посчитать площадь треугольника по формуле Герман:
#S = sqrt(p * (p-a) * (p-b) * (p-c))
#Где p = (a + b+ c) / 2 - полупериметр треугольника
#Сделать 3 варианта возведения в степень
import math

a = float(input("Enter a:  "))
b = float(input("Enter b:  "))
c = float(input("Enter c:  "))

p = (a + b + c) / 2

S = round(((p * (p-a) * (p-b) * (p-c))**0.5), 2)
print(S)

S = round(pow((p * (p-a) * (p-b) * (p-c)), 1/2), 2)
print(S)

S = round(math.pow((p * (p-a) * (p-b) * (p-c)), 1/2), 2)
print(S)

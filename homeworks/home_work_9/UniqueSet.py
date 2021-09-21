#2. Напишите программу, которая принимает два набора и выводит все элементы первого, которых нет во втором.
import random

a = {random.randint(0, 50) for i in range(10)}
b = {random.randint(0, 50) for i in range(10)}

print(a-b)
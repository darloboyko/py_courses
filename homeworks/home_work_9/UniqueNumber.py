#3. Написать программу, которая на вход принимает список чисел и проверяет, 
#все ли числа в этой последовательности уникальны

import random

i = 10
lst_1 = []

while i > 0:
    lst_1.append(random.randint(0, 100)) 
    i -= 1
print(lst_1)

print("True") if len(set(lst_1)) == len(lst_1) else print("False")   
    
    



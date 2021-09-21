#3. Написать программу, которая на вход принимает список чисел и проверяет, 
#все ли числа в этой последовательности уникальны

n = int(input("Entel len list: "))
i = 0
lst_1 = []

while i < n:
    elem = int(input("Enter element: "))
    lst_1.append(elem) 
    i += 1
#lst_1 = [12, 45, 34, 1, 2, 3, 4, 5, 89]

print("True") if len(set(lst_1)) == len(lst_1) else print("False")   
    
    



#Написать программу, которая сравнивает два числа типа int и определяет, 
# какое из чисел большее, а какое меньшее. 
# Программа должна вывести что-то типа “The number x has the greatest value”. 
# Где “x” одно из чисел

a = int(input("a:  "))
b = int(input("b:  "))

x = a if a > b else b
print("The number", x, "has the greatest value")
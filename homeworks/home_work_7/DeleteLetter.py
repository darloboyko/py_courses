#1. Написать программу, в которой необходимо удалить все указанные буквы из строки
#Строку и букву (или несколько) ввести с клавиатуры.

a = input("Enter string: ")
b = input("Enter letter: ")

c = a.replace(b, "")

print(c)
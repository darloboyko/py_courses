#Напишите программу, которая выведет все числа Фибоначчи до заданного числа
#Например, пользователь вводит 100
#Ответ: 1 1 2 3 5 8 13 21 34 55 89

x = int(input("Enter x:  "))

a = b = 1
print(a, b, end=" ")
while a + b <= x:
  a,b = b,a+b
  print(b, end=" ")

  
#5. Напишите программу, которая выведет все числа из списка, которые делятся на заданное число
#Число задавать с клавиатуры, список задать в самой программе (как в прошлых заданиях)

n = int(input("Enter n:  "))
lst = [20, 43, 58, 16, 157, 180, 45, 67, 87, 33]

for i in lst:
 if i%n == 0:
   print(i, end=" ")
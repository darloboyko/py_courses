
#Написать программу, которая бы решала уравнение вида a x + b = 0 
# Переменные a и b можно задать вручную. Далее нужно будет посчитать и вывести значение “х”.
# Программа должна также учитывать варианты, когда или а = 0 или b = 0

a = float(input("a:  "))
b = float(input("b:  "))

if a == 0 and b == 0:
    print("Endless number of solutions")
elif a == 0 and b != 0:
    print("No solution")
else:
    x = -b/a
    print("x =", x)
#4. Написать программу, которая построит псевдо бинарную строку.
#Будет дана строка, которая состоит только из цифр (сделать соответствующую проверку)
#Нужно заменить все числа, которые меньше 5 на 0, остальные, которые равны 5 и больше на 1
#Ответом будет одна строка
#Начальную строку ввести с клавиатуры
#Пример: 47569386590
#Ответ: 01111011110

s = input("Enter string: ")
b_lst = []
if s.isdigit():
    s = list(s)
    s = [int(i) for i in s]
    for i in s:
        b_lst.append(0 if i < 5 else 1)
        b_lst_1 = ''.join(str(i) for i in b_lst)
    print(b_lst_1)
else:
    print("Error")   
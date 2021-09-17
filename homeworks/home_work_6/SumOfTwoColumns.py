#5. Написать программу, которая считает сумму двух колонок. Если одна из колонок имеет больший размер 
# - вывести, какая колонка больше. Если колонки одинаковы, вывести результат так:
# | row_1 | row_2 | sum |
# |  2 | 5 | 7 |

row_1 = [1, 2, 5, 6, 54]
row_2 = [11, 5, 5, 7, 3]

if len(row_1) == len(row_2):
    for i in range(0, len(row_1)): 
        print("|",row_1[i],"|",row_2[i],"|", row_1[i]+row_2[i], "|")
elif len(row_1) > len(row_2):
    print("The row_1 biggest")
else:
    print("The row_2 biggest") 
  


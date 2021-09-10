#5. Написать программу, которая считает сумму двух колонок. Если одна из колонок имеет больший размер 
# - вывести, какая колонка больше. Если колонки одинаковы, вывести результат так:
# | row_1 | row_2 | sum |
# |  2 | 5 | 7 |

row_1 = [1, 2, 5, 6]
row_2 = [11, 5, 5, 7]

if len(row_1) == len(row_2): 
    row_sum = sum(row_1)+sum(row_2)
    print("|",sum(row_1),"|",sum(row_2),"|", row_sum, "|")
elif len(row_1) > len(row_2):
    print("The row_1 biggest")
else:
    print("The row_2 biggest") 
  


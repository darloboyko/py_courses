#3. Написать программу, которая посчитает сумму всех элементов в списке
#Список задать в самой программе в виде: list = [1, 5, 68, 0]
#В нем может быть сколько угодоно элементов

lst = [23, 45, 65, 4, 2, 87, 95]

sum_numbers = 0
for i in lst:
     sum_numbers += i
print(f"Sum of all numbers in the list: {sum_numbers}")
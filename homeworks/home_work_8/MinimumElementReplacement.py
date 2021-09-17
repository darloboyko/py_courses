#3. Найти среднее арифметическое значение всех отрицательных элементов в списке. 
# Заменить минимальный элемент в этом списке на это среднее арифметическое


lst = [1, -30, 4, 45, -78, 7, -55, 23, 11, -15, -130, 22, -35]
new_list_neg = []

for i in lst:
    if i<0:
        new_list_neg.append(i)
        mid_sum = round((sum(new_list_neg)/len(new_list_neg)), 1)
lst[lst.index(min(lst))] = mid_sum
print(lst)


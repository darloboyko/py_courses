#3. Найти среднее арифметическое значение всех отрицательных элементов в списке. 
# Заменить минимальный элемент в этом списке на это среднее арифметическое


lst = [1, -3, 4, 45, -36, 7, -95, 23, 11, -45, -13, 22, -35]
new_list_neg = []
for i in range(len(lst)):
    if min(lst) == lst[i]:
        lst[i] = mid_sum_lst
        break
    if lst[i]<0:
        new_list_neg.append(lst[i])
        mid_sum_lst = round((sum(new_list_neg)/len(new_list_neg)), 1)
print(lst)



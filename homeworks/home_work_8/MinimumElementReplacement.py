#3. Найти среднее арифметическое значение всех отрицательных элементов в списке. 
# Заменить минимальный элемент в этом списке на это среднее арифметическое


lst = [1, -3, 4, 45, 47, 7, -55, 23, 11, -15, -13, 22, -35]
new_list_neg = []
for i in range(len(lst)):
    if lst[i]<0:
        new_list_neg.append(lst[i])
        mid_sum = round((sum(new_list_neg)/len(new_list_neg)), 1)
        print(mid_sum)
    if min(lst) == lst[i]:
        lst[i] = mid_sum
        break
print(lst)



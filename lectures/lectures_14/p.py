def sum_lst(lst):
    sum_1 = lst[0]
    if len(lst) == 1:
        return lst[0]
    else:
        return sum_1 + sum_lst(lst[1:]) 


lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(sum_lst(lst))




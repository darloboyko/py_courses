




def numbe_convert_to_dict(lst_1, lst_2):
    dict = {}
    for i in lst_1:
        dict[lst_1[i]]=lst_2[i] 
    return dict


num = str(input("Enter num: "))

lst_1 = [1,2,3,4,5,6,7,8,9,0]
lst_2 = [9,8,7,6,5,4,3,2,1,0]

p = (numbe_convert_to_dict(lst_1, lst_2))

n = lambda : list(key for key in p if p[key] == num)
print(n)

#print(list(map((key for key in p if p[key] == num), p)))
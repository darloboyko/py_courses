lst = [1, 2, 3, 4, 5]
fold_number = 3
i = 1

while i <= fold_number:
   lst_1 = []
   index = 0
   length = len(lst)
   mediana = length//2 + length%2
   while index < mediana:
      if index == (length-1-index):
         lst_1.append(lst[index])
      else:      
         lst_1.append(lst[index] + lst[-1-index]) 
      index+=1
   lst = lst_1.copy()  
   i+=1
print(lst_1)
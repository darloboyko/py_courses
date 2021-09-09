lst = [7, 8, 9, 10, 11, 12, 13]
i = 1
while i < len(lst):
    if lst[i] != lst[i-1] + 1:
          print(lst[i])
          break
    i +=1
else:
    print("ok")
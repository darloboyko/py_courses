a = int(input ("Enter a:  "))

lst = []
while a >= 0:
    lst.append(a)
    a -= 1

print(lst)

for i in range(0, a+1):
    lst.append(i)
    lst.reverse()
print(lst)
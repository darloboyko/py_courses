s = input("Enter string: ")
lst_palindrom = list(s)
p = lst_palindrom.count(' ') 

while p > 0:
    lst_palindrom.remove(' ')
    p-=1

if lst_palindrom[:] == lst_palindrom[::-1]:
	print("It is palindrom")
else:
	print("It is not palindrom")


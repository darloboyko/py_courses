s = input('Enter string: ')

#list(s)[1: len(s)-1]
#print(list(s))

list_str = list(s)
list_str.pop(0)
list_str.pop(-1)
print(list_str)
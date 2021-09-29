#Complete the function that takes two integers (a, b, where a < b) and return an array of all 
# integers between the input parameters, including them.
##For example:
#a = 1
# b = 4
# --> [1, 2, 3, 4]

def fromNumbeList(a, b):
    lst = []
    while a != b+1:
        lst.append(a)
        a+=1
    return lst
    

a = int(input("a: "))
b = int(input("b: "))

print(fromNumbeList(a, b)) 
print(fromNumbeList(-4, 7)) 
print(fromNumbeList(7, 18)) 
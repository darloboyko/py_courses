a = input("Enter string: ")

i = 0
while i < len(a):
    a = a[1:]+a[0]
    print(a)
    i += 1

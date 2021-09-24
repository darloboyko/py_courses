s = (input("Enter string: ")).split()

dct = {}

for i in s:
    if len(i) not in dct:
        dct[len(i)] = 1
    else:
        dct[len(i)] += 1
print(dct)


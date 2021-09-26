def my_func(s):
        return [ord(c) for c in s]


s = str(input("Enter string: "))

print(my_func(s))
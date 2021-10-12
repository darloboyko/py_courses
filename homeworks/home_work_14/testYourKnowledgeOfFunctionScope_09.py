#Write a function that adds from two invocations.
#All inputs will be integers.
#add(3)(4)  // 7
#add(12)(20) // 32


add = lambda a: lambda b: a + b 


print(add(3)(4))
print(add(34)(6))
print(add(5)(5))
print(add(25)(54))
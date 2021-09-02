#Написать программу которая будет сравнивать величину (magnitude) двух чисел. 
# Например, если одно число = 3, а второе число = -9, программа должна выдать, 
# что число -9 имеет большую величину

a = int(input("Enter a:  "))
b = int(input("Enter b:  "))

x = a if abs(a) > abs(b) else b
print("The magnitude number", x , "is the bigest")
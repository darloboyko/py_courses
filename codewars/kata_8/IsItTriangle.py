#Implement a function that accepts 3 integer values a, b, c. 
#The function should return true if a triangle can be built with the sides of given length 
#and false in any other case.
#(In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    if abs(a) < (abs(b) + abs(c)) and abs(b) < (abs(a) + abs(c)) and abs(c) < (abs(b) + abs(a)):
        return True
    else:
        return False


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(is_triangle(a, b, c))
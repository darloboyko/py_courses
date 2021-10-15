#Expansion is performed for a given 2x2 matrix.
# 
#[
#  [1,2],
#  [5,3]
#]
#After expansion:
#[
#  [1,2,a],
#  [5,3,b],
#  [c,d,e]
#]
#a = 1 + 2 = 3
#b = 5 + 3 = 8
#c = 5 + 1 = 6
#d = 3 + 2 = 5
#e = 1 + 3 = 4
#Final result:
#[
#  [1,2,3],
#  [5,3,8],
#  [6,5,4]
#]
#TASK
#Let expansion be a function which takes two arguments:
#A: given NxN matrix
#n: number of expansions
#https://www.codewars.com/kata/614adaedbfd3cf00076d47de/train/python

def expansion(matrix, n=0): 
    for i in range(len(matrix)):
        print(i)
        matrix[i].append(sum(matrix[i]))
        
   # for i in range(len(matrix)+1+n): 
        #print(i)
      #  matrix.append(list(map(sum, zip(matrix[i],matrix[i+n]))))
        #matrix[len(matrix)-1][len(matrix)-1] = matrix[0][0]+matrix[len(matrix)-2][len(matrix)-2]
        #print(len(matrix))        
    return print(matrix)


matrix = [
    [1, 3, 4],
    [2, 5, 6],
    [5, 2, 1]
]
n = int(input("Enter number: "))

print(expansion(matrix, n))
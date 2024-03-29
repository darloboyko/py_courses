#Scenario
#Several people are standing in a row divided into two teams.
#The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.
#Task
#Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, 
# where the first one is the total weight of team 1, and the second one is the total weight of team 2.
#Notes
#Array size is at least 1.
#All numbers will be positive.
#Input >> Output Examples
#rowWeights([13, 27, 49])  ==>  return (62, 27)
#Explanation:
#The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.
#rowWeights([50, 60, 70, 80])  ==>  return (120, 140)




row_weights = lambda array: (sum(array[::2]), sum(array[1::2]))

array = [50, 60, 70, 80]

print(row_weights(array))
print(row_weights([13, 27, 49]))
print(row_weights([13, 24, 45, 62, 27, 49]))


    
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


def row_weights(array):
    first_tim  = []
    second_tim  = []
    for i in range(0, len(array)):
        if i%2 != 0:
            second_tim.append(array[i])
        else:
            first_tim.append(array[i])
    return sum(first_tim), sum(second_tim)

array = [50, 60, 70, 80]
print(row_weights(array))

#row_weights = lambda array: (sum(array[::2]), sum(array[1::2]))

#print(row_weights(array))


    
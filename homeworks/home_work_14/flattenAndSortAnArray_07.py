#Challenge:
#Given a two-dimensional array of integers, return the flattened version of the array 
# with all the integers in the sorted (ascending) order.
#Example:
#Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

from functools import reduce

flatten_and_sort = lambda array: sorted(reduce(lambda c, x: c + x, array, []))


array = [[9,8,7],[],[3,2,1]]

print(flatten_and_sort(array))
print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))
print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))








#A Nice array is defined to be an array where for every value n in the array, there is also an 
# element n-1 or n+1 in the array.
#example:
#[2,10,9,3] is Nice array because
#2=3-1
#10=9+1
#3=2+1
#9=10-1
#Write a function named isNice/IsNice that returns true if its array argument is a Nice array, else false. 
# You should also return false if input array has no elements.

#https://www.codewars.com/kata/59b844528bcb7735560000a0/train/python
arr = [2,10,9,3]

is_nice = lambda arr: sorted(arr)

map(is_nice, arr)

"even" if sum(arr)%2 == 0 else "odd"

print(is_nice(arr))
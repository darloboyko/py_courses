#This question is a variation on the Arithmetic Progression kata
#The following was a question that I received during a technical interview for an entry 
# level software developer position. I thought I'd post it here so that everyone could give it a go:
#You are given an unsorted array containing all the integers from 0 to 100 inclusively. 
# However, one number is missing. Write a function to find and return this number. 
# What are the time and space complexities of your solution?

def missing_no(nums):
    nums.sort()    
    for i in range(0, len(nums)-1):
        if nums[0] != 0:
            return 0
        elif abs(nums[i] - nums[i+1]) == 1:
            continue
        elif abs(nums[i] - nums[i+1]) != 1:
            return nums[i]+1
    return 100

print(missing_no([1, 6, 4, 7, 8,  0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 2, 3, 5, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
print(missing_no([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0, 1, 2, 3, 4, 5, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))


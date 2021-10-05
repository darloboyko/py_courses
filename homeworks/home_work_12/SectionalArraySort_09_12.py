#In this kata you are given an array to sort but you're expected to start sorting from 
#a specific position of the array (in ascending order) and optionally you're given the number 
#of items to sort.
#Examples:
#sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 2) //=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
#sect_sort([9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5) //=> [9, 7, 1, 2, 3, 4, 5, 8, 6]
#Documentation:
#sect_sort(array, start, length);
#array - array to sort
#start - position to begin sorting
#length - number of items to sort (optional)
#if the length argument is not passed or is zero, you sort all items to the right of the start 
#postiton in the array

def sect_sort(array, start=0, length=0):
    if length:
        return array[:start:] + sorted(array[start:start+length:]) + array[start+length:]
    return array[:start:] + sorted(array[start:])


array = [2, 4, 6, 8, 1, 5, 7]
start = int(input("Enter start: "))
length = int(input("Enter length: "))

print(sect_sort(array,start,length))  
print(sect_sort([1, 2, 4, 6, 8, 10, 5, 7], 3))
print(sect_sort([12, 14, 6, 8, 1, 15, 7, 9, 11], 2, 4))
print(sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 5))
print(sect_sort([9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5))
print(sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 8, 3))
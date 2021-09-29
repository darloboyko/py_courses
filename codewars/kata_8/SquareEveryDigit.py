#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
##For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#Note: The function accepts an integer and returns an integer

def square_digits(num):
    lst_num = []
    for number in list(str(num)):
        lst_num.append(pow(int(number), 2))
        lst_num_1 = ''.join(str(number) for number in lst_num)
    return int(lst_num_1)
  
     
num = int(input("Enter number: "))

print(square_digits(num))
print(square_digits(1245))
print(square_digits(8766))
print(square_digits(3458))
print(square_digits(8531))


#def square_digits(n):
 # return int("".join(str(pow(int(i), 2)) for i in str(n)))
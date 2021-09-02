#Написать программу с названием “CheckOddEven”, 
# которая печатает “Odd Number” если переменная “number” 
# типа int нечетная. Или “Even Number” если переменная четная. 
# Программа всегда должна перед выходом печатать “BYE”

number = int(input("number:  "))

if number%2 == 1:
    print("Odd Number")
else:
 print("Even Number")  
 
print("BYE \n")
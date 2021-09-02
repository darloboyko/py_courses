#Написать программу с названием “PrintDayInWord”, 
# которая печатает “Sunday”, “Monday”, …. “Saturday”, 
# если переменная “day” типа int будет 1, 2, 3, 4 … 7. 
# В противном случае программа должна вывести “Not a valid day”.

number = int(input("number:  "))

if number == 1:
 print("Sunday")
elif number == 2:
 print("Monday")
elif number == 3:
 print("Tuesday")
elif number == 4:
 print("Wednesday")
elif number == 5:
 print("Thursday")
elif number == 6:
 print("Friday")
elif number == 7:
 print("Saturday")
else:
 print("Not a valid day")
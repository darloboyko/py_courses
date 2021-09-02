#Написать программу с названием “PrintNumberInWord”, 
# которая напечатает “ONE”, “TWO”, …, “NINE”, 
# “OTHER” если переменная “number” типа int будет 1, 2, 3, 4, … 9, или любой другой.

number = int(input("number:  "))

if number == 1:
 print("ONE")
elif number == 2:
 print("TWO")
elif number == 3:
 print("THREE")
elif number == 4:
 print("FOUR")
elif number == 5:
 print("FIVE")
elif number == 6:
 print("SIX")
elif number == 7:
 print("SEVEN")
elif number == 8:
 print("EIGHT")
elif number == 9:
 print("NINE")
else:
 print("OTHER \n")
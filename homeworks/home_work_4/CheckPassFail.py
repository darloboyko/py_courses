#Написать программу с названием “CheckPassFail”, 
# которая выводит PASS если переменная “mark” типа int больше 
# или равно 50 или вывести “FAIL” в противном случае. 
# Программа всегда должна перед выходом печатать “DONE”

mark = int(input("mark:  "))

if mark >= 50:
    print("PASS")

else: 
    print("FAIL")

print("DONE")
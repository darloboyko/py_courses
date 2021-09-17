#1. Написать простую классическую игру с угадыванием чисел
#Компьютер загадывает любое число в диапазоне от 1 до 50 и дает 6 попыток отгадать это число. 
#Когда пользователь вводит число, компьютер проверяет, угадано ли число и если не угадано, 
#сообщает пользователю меньше ли или больше загаданное число. Если пользователь угадал - то сообщает, 
#что число угадано. Для "загадывания" число используйте такой код:
#import random
#secret_number = ranomd.randomint(1, 50)

import random
secret_number = random.randint(1, 50)
your_number = 0
i = 6

while your_number !=  secret_number:
    while i != 0:
        your_number = int(input(f"You have {i} attempts left. Enter a number from 1 to 50: "))
        if 1 <= your_number <= 50:
            if secret_number < your_number:
                print("The entered number is greater than intended")
            elif secret_number > your_number:
                print("The entered number is less than intended")
            elif secret_number == your_number:
                print(f"Win! You guessed the number",secret_number)
                break
            i-=1 
        else:
            print("Error")
            break  
    break

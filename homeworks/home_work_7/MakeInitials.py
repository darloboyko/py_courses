#3. Написать программу, которая будет возвращать инициалы человека:
#Sam Harris => S.H.
#Patrick Feeney => P.F.
#Имя Фамилию ввести с клавиатуры.
#Сделать проверку на количество введенных слов (должно быть точно 2), 
# а также проверку, что введенный текст валидный (что там нет цифр)

first_last_name = input("Enter First Name and Last Name: ")
if len(first_last_name.split()) == 2 and first_last_name.replace(' ', "").isalpha(): 
    print(list(first_last_name.split()[0])[0], list(first_last_name.split()[1])[0], sep=".", end=".")
else:
    print("Error")   
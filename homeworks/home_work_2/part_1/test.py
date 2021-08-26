#написать программу, которая посчитает процент правильно решенных заданий 
# Задано два числа - общее количество вопросов и число правильно отвеченных 
# вопросов
questions =int(input("Enter the numbers of questions:  "))
answers = int(input("Enter the number of correct answers:  "))

percent = (answers/questions)*100

print("Percentage of correct answers", round(percent, 2), " %")
#3. Посчитать количество оценок в классе. Ввести список из 30 элементов от 0 до 100.
#Ответом будет словарь вида:
#marks = {
#  'A' : 6,
#  'B' : 10,
#  'C' : 4,
#  'D' : 6,
#  'E' : 0
#}
#Градаци оценок:
#90 < A <= 100
#80 < B <= 90
#70 < C <= 80
#60 < E <= 70
#D <= 60
import random

i = 30
points = []

while i > 0:
    points.append(random.randint(0, 100)) 
    i -= 1

marks = dict.fromkeys(['A', 'B', 'C', 'D', 'E'], 0)

for n in range(0, len(points)):
    if  90 <= points[n] <= 100:
        marks['A'] += 1
    elif  80 <= points[n] < 90:
        marks['B'] += 1
    elif  70 <= points[n] < 80:
       marks['C'] += 1
    elif  60 <= points[n] < 70:
        marks['D'] += 1
    elif  0 <= points[n] < 60:
        marks['E'] += 1
print(marks)

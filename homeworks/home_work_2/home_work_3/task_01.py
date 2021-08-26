#Вывести текущее время из миллисекунд в виде дни:часы:минуты:секунды
#Получить текущее время в миллисекундах:

import time

current_time_millis = round(time.time()* 1000)

a = time.strftime("%d:%H:%M:%S", time.localtime())

print(a)
print("Current time in millis:", current_time_millis)



#Вывести текущее время из миллисекунд в виде дни:часы:минуты:секунды
#Получить текущее время в миллисекундах:

import time

current_time_millis = round(time.time()* 1000)
day = current_time_millis // (3600*1000*24)
hours = (current_time_millis % (3600*1000*24)) // (3600*1000)
minute = (current_time_millis % ((day*24 + hours)*3600*1000)) // (60*1000)
seconds =  (current_time_millis % ((day*24*3600 + hours*3600 + minute*60)*1000)) // (1000)

print(day,":",hours,":",minute,":",seconds)
print("Current time in millis:", current_time_millis)



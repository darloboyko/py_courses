#2. Фермеры пытаются бороться с волками. К счастью, фермеры отлично отличают волков.
#Написать программу, которая будет выводить строку, предупреждая овцу, перед которой стоит волк. 
#Если перед волком никого нет, вывести строку прогоняя волка
#Список начинается с конца
#Примеры:
# ["sheep", "sheep", "sheep", "wolf", "sheep"] == 'Oi! Sheep number 1! You are about to be eaten by a wolf!'
#['sheep', 'sheep', 'wolf'] == 'Pls go away and stop eating my sheep'

lst =["sheep", "sheep", "sheep","wolf", "sheep", "sheep", "sheep",  "sheep"]
#lst.reverse()
#wolf_index = lst.index("wolf")

#if wolf_index == 0:
  #  print("Pls go away and stop eating my sheep")  
#else:
   #print(f'Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!')

i = 0
#lst =["sheep", "sheep", "sheep", "sheep", "sheep", "sheep", "sheep", "wolf", "sheep"]
lst.reverse()
while i <= len(lst):
    if lst[i] == "wolf":
        print("Pls go away and stop eating my sheep")
    elif lst[i] == "sheep":
        i+=1           
print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!') 





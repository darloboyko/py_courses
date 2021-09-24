#1 Посчитать разницу в возрасте между самым старым и самым молодым членом семьи
#Вводные условия:
#Словарь может отличаться наличием или отсутствием ключей. 
#Так что лучше не привязываться к определенным ключам

family = {
  'grandpa': ('Alex', 76),
  'grandma': ('Nona', 74),
  'dad': ('Greg', 48),
  'mom': ('July', 45),
  'son_older': ('Bob', 18),
  'son_middle': ('Alex', 15),
  'son_young' : ('Mark', 10)
}

dif_age =[]
for i in family.values():
    dif_age.append(i[1])
print(max(dif_age)-min(dif_age))









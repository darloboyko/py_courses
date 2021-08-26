#Смешано V1 литров воды с температурой T1 и V2 литров с температурой T2. 
# Написать программу, которая посчитает объем и температуру получившейся 
# смеси Считается по формуле (v1*t1 + v2*t2) / (v1 + v2)

v1 = int(input("Enter v1, ml:  "))
t1 = int(input("Enter t1, C:  "))
v2 = int(input("Enter v2, ml:  "))
t2 = int(input("Enter t2, C:  "))

mix_temperature = ((v1*t1 + v2*t2) / (v1 + v2))
mix_volume = v1 + v2

print("The temperature of the mixture", round(mix_temperature, 2), "C")
print("The volume of the mixture", round(mix_volume, 2), "ml") 
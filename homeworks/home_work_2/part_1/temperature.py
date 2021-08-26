# Написать программу, которая умеет переводить температуру из C в из Фаренгетов и Кельвинов Например:
# дана температура в Цельсиях 25 С
# Фаренгейт: 45.9F - считается по формуле (C + 32) * 5/9
# Кельвины: 298.16K - считается по формуле C + 273.16

print("Temperature converter")

temperature_сelsius = int(input("Enter temperature_сelsius:  "))

temperature_kelvin = (temperature_сelsius + 273.16)
temperature_fahrenheit = (temperature_сelsius * 9/5 +32)

print("Temperature in Kelvin:", round(temperature_kelvin, 2), "K")
print("Temperature in Fahrenheit:", round(temperature_fahrenheit, 2), "F")


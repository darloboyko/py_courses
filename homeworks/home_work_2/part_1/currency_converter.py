#написать программу для подсчет конвертации валюты: UAH --> USD
#USD --> UAH
#UAH --> EUR
#EUR --> UAH
uah = int(input("Enter uah:  "))
usd = int(input("Enter usd:  "))
eur = int(input("Enter eur:  "))


uah_usd = uah / 26.8
usd_uah = usd * 26.45 
uah_eur = uah / 31.34
eur_uah = eur * 30.9


print("UAH --> USD:", round(uah_usd, 1))
print("USD --> UAH:", round(usd_uah, 1))
print("UAH --> EUR:", round(uah_eur, 1))
print("EUR --> UAH:", round(eur_uah, 1))
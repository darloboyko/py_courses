import random

partition = 1000

i = 0
skipped = 0 
while i < 3000:
    rain_poss = random.random() 
    if rain_poss > 0.95:
        print(f"Rain possibility: {rain_poss}")
        print("Run home..")
        break 

    if i % 1000 == 0 and i != 0:
        print("Drink..")

    print("Run..") 

    i+=200  

print("Rest..")
print(i)
print(i-skipped)


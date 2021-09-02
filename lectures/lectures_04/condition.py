print("Let's calculate BMI")

weight = float(input("Enter weight:  "))
height = float(input("Enter height:  "))
bmi = round(weight / (height*height), 1)

print("BMI =", bmi)

if bmi <= 20:
    print("Underweight")
elif 20 < bmi <= 30:
    print("Normal") 
elif 30 < bmi <= 40:
    print("Extra")  
elif bmi > 40:
    print("Obesity")   


  

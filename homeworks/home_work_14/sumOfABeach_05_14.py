#Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times 
#the words "Sand", "Water", "Fish", and "Sun" appear without overlapping (regardless of the case).
#Examples
#sum_of_a_beach("WAtErSlIde")                    ==>  1
#sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
#sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
#sum_of_a_beach("cItYTowNcARShoW")               ==>  0


sum_of_a_beach = lambda c_beach: c_beach.lower().count("sand")+c_beach.lower().count("water")+c_beach.lower().count("fish")+c_beach.lower().count("sun")


beach = str(input("Enter string: "))

print(sum_of_a_beach(beach))
print(sum_of_a_beach("SanD"))
print(sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN"))
print(sum_of_a_beach("gOfIshsunesunFiSh"))
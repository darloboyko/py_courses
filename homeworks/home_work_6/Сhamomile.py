#1. Есть старая игра с "гаданием" на лепестках - выдергивая лепесток произносится одна из фраз:
# I love you - a little - a lot - passionately - madly - not at all 
# Написать программу, которая будет принимать количество лепестков и потом выдавать, 
# какая фраза выпала на последний лепесток Количество лепестков всегда больше 0

petal = int(input("Enter number of petals: "))

if petal%6 == 0:
    print("not at all")
elif petal%6 == 5:
    print("madly")
elif petal%6 == 4:
    print("passionately")
elif petal%6 == 3:
    print("a lot")
elif petal%6 == 2:
    print("a little")
elif petal%6 == 1:
    print("I love you")


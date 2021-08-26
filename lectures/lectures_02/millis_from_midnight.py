print("Let's calculate milliseconds from midnight")

hours=int(input('Enter current hour:  '))
minutes=int(input('Enter current minutes:  '))
seconds=int(input('Enter current seconds:  '))

millis = (seconds+minutes*60+seconds*3600)*1000

print(millis, "")

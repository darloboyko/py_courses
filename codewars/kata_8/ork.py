def disemvowel(string_):
    for i in 'aeuioAEUIO': 
        string_ = string_.replace(i,"")
    return string_


string_ = str(input("Enter: "))

print(disemvowel(string_)) 
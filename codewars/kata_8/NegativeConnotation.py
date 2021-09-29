#You will be given a string with sets of characters, (i.e. words), seperated by between one and 
# three spaces (inclusive).
#Looking at the first letter of each word (case insensitive-"A" and "a" should be treated the same), 
# you need to determine whether it falls into the positive/first half of the alphabet ("a"-"m") 
# or the negative/second half ("n"-"z").
#Return True/true if there are more (or equal) positive words than negative words, False/false otherwise.
#"A big brown fox caught a bad rabbit" => True/true
#"Xylophones can obtain Xenon." => False/false

def connotation(strng):
    positive = 0
    negative = 0
    strng = strng.replace(' ','').upper()
    for alphabet in strng:
        if alphabet == ("a", "m"):
            positive +=1
            print(positive)
        elif alphabet == (("n", "z")):    
           negative +=1
           print(negative)
    return  True if  positive > negative else False


strng = str(input("String: "))

print(connotation(strng))  
print(connotation("All FOoD tAsTEs NIcE for someONe"))
print(connotation("CHOCOLATE MAKES A GREAT SNACK"))
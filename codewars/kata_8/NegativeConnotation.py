#You will be given a string with sets of characters, (i.e. words), seperated by between one and 
# three spaces (inclusive).
#Looking at the first letter of each word (case insensitive-"A" and "a" should be treated the same), 
# you need to determine whether it falls into the positive/first half of the alphabet ("a"-"m") 
# or the negative/second half ("n"-"z").
#Return True/true if there are more (or equal) positive words than negative words, False/false otherwise.
#"A big brown fox caught a bad rabbit" => True/true
#"Xylophones can obtain Xenon." => False/false

def connotation(strng):
    strng = list(strng.replace(' ','').upper())
    newstring = "".join(c for c in strng if c.isalpha())
    print(newstring)
    positive = 0
    negative = 0
    chars_p = list('ABCDEFGHIJKLM')
    chars_n = list('NOPQRSTUVWXYZ')
    for i in newstring:
        if i in chars_p:
            positive += 1           
        elif i in chars_n:
            negative += 1                 
    return positive >= negative


strng = str(input("String: "))

print(connotation(strng))  
print(connotation("Xylophones     can obtain Xenon."))
print(connotation("A big brown fox caught a123456123!@#$ bad bunn"))
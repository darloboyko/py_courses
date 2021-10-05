#You will be given a string with sets of characters, (i.e. words), seperated by between one and 
# three spaces (inclusive).
#Looking at the first letter of each word (case insensitive-"A" and "a" should be treated the same), 
# you need to determine whether it falls into the positive/first half of the alphabet ("a"-"m") 
# or the negative/second half ("n"-"z").
#Return True/true if there are more (or equal) positive words than negative words, False/false otherwise.
#"A big brown fox caught a bad rabbit" => True/true
#"Xylophones can obtain Xenon." => False/false
#https://www.codewars.com/kata/5ef0456fcd067000321baffa/train/python

def connotation(strng):
    strng = list(strng.replace(' ','').lower())
    newstring = "".join(c for c in strng if c.isalpha())
    positive = 0
    chars_p = list('abcdefghijklm')
    for i in newstring:
        if i in chars_p:
            positive += 1                         
    return positive >= (len(newstring)-positive)


strng = str(input("String: "))

print(connotation(strng))  
print(connotation("Xylophones     can obtain Xenon."))
print(connotation("A big brown fox caught a123456123!@#$ bad bunn"))
print(connotation("A big brown fox caught a bad rabbit"))
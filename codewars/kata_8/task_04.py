#Your task is to make a program takes in a sentence (without puncuation), adds all words to a 
# list and returns the sentence as a string which is the positions of the word in the list. 
# Casing should not matter too.
##Example
# "Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"
# becomes
# "01234567802856734"
# Another example
# "the one bumble bee one bumble the bee"
# becomes
# "01231203"

def compress(sentence):
    for i in range(0, len(sentence)):
        lst = []
        lst.append(i)
        if i == lst[i]:
            lst.append(i)
        print(lst)
    return lst
    
sentence = str(input("Enter your string: ")).upper().split()

print(compress(sentence))
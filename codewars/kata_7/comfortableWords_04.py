#A comfortable word is a word which you can type always alternating the hand you type with 
#(assuming you type using a QWERTY keyboard and use fingers as shown in the image below).
#That being said, create a function which receives a word and returns true/True if it's a 
# comfortable word and false/False otherwise.
#The word will always be a string consisting of only ascii letters from a to z.
#To avoid problems with image availability, here's the lists of letters for each hand:
#Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
#Right: y, u, i, o, p, h, j, k, l, n, m

def comfortable_word(word):
    result  = []
    left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
    right = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']

    for i in word.lower():
        if i in left:
            result.append('left')      
        elif i in right:
            result.append('right')
    print(result)
    for n in range(1, len(result)):
        if result[n-1] == result[n]:
            return False
        else:
            continue
    return True
       

#word = str(input("Word: "))

#print(comfortable_word(word))  
print(comfortable_word("lalalalalalalal"))
#print(comfortable_word("A big brown fox caught a123456123!@#$ bad bunn"))
#print(comfortable_word("A big brown fox caught a bad rabbit"))
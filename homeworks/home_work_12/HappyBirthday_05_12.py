#It's your best friend's birthday! You already bought a box for the present. 
# Now you want to pack the present in the box. You want to decorate the box with a ribbon and a bow.
#But how much cm of ribbon do you need?
#Write the method wrap that calculates that!
#A box has a height, a width and a length (in cm). The ribbon is crossed on the side with the largest area. 
# Opposite this side (also the side with the largest area) the loop is bound, calculate with 20 cm more tape.
#  wrap(17,32,11) => 162
#  wrap(13,13,13) => 124
#  wrap(1,3,1) => 32
#Notes:
#height, width and length will always be >0
#The ribbon and the bow on the present looks like this:

def wrap(height, width, length):
    p = (height, width, length)
    return 2*max(list(p))+4*min(list(p))+2*(sum(list(p))-(max(list(p))+min(list(p))))+20


height = int(input("Enter height: "))
width = int(input("Enter width: "))
length = int(input("Enter length: "))

print(wrap(height, width, length))  
print(wrap(120, 23, 25))
print(wrap(24, 45, 56))
print(wrap(17,32,11))
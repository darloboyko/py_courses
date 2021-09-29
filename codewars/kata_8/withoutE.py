#Is it possible to write a book without the letter 'e' ?
#Task
#Given String str, return:
#How much "e" does it contains (case-insensitive) in string format.
#If given String doesn't contain any "e", return: "There is no "e"."
#If given String is empty, return empty String.
#If given String is `null`/`None`/`nil`, return `null`/`None`/`nil`

def find_e(s):
    n = 0
    print(s)
    if s == '': 
        return ''
    if s == None:
        return None
    if 'E' in s.replace(' ','').upper():
            for i in s.replace(' ','').upper():
                 if i == 'E':
                    n+=1              
            return str(n)     
    else:
        return 'There is no "e".'                    


s = str(input("Enter your string: "))

print(find_e(s))
print(f'Contains "e", {find_e("EEEeeeeee Etyui sedcth")}')
print(f'String is empty, {find_e("")}')
print(f'There is no "e", {find_e("sdfghj cvghiu uhgcx ujhnbgv")}')
print(f'String is None, {find_e(None)}')

#Let's assume we need "clean" strings. Clean means a string should only contain letters a-z, A-Z and spaces.
#  We assume that there are no double spaces or line breaks.
#Write a function that takes a string and returns a string without the unnecessary characters.
#Examples
#remove_chars('.tree1')    ==> 'tree'
#remove_chars("that's a pie$ce o_f p#ie!")  ==> 'thats a piece of pie'
#remove_chars('john.dope@dopington.com')    ==> 'johndopedopingtoncom'
#remove_chars('my_list = ["a","b","c"]')    ==> 'mylist  abc'
#remove_chars('1 + 1 = 2')    ==> '    ' (string with 4 spaces)
#remove_chars("0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_")  ==> '' (empty string)

remove_chars = lambda s:''.join((filter(lambda chars: chars not in list("\":\\'`0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_"), list(s))))


s = str(input("Enter string: "))

print(remove_chars(s))
print(remove_chars("test for error!"))
print(remove_chars(".tree1"))
print(remove_chars("john.dope@dopington.com"))
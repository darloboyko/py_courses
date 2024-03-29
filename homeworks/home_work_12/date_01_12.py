#Write a function that receives two strings as parameter. This strings are in the following 
#format of date: YYYY/MM/DD. Your job is: Take the years and calculate the difference between them.
#Examples:
#'1997/10/10' and '2015/10/10' -> 2015 - 1997 = returns 18 
#'2015/10/10' and '1997/10/10' -> 2015 - 1997 = returns 18
#At this level, you don't need validate months and days to calculate the difference.

def how_many_years (date1,date2):
    date1 = (date1.split('/'))
    date2 = (date2.split('/'))
   
    return abs(int(date1[0]) - int(date2[0]))


date1 = str(input("Enter date 1: "))
date2 = str(input("Enter date 2: "))

print(how_many_years(date1, date2)) 
print(how_many_years('1997/10/10', '2015/10/10')) 
print(how_many_years('2015/10/10', '1997/10/10')) 
from datetime import date, datetime
import os

def read_file(src):
    return open(src, 'r')


def data_convert_to_dict(f):
    dictDate = {}
    for line in f:
        date = line.strip().split(',')
        dictDate[date[0]]=date[1]  
    return dictDate    


def return_count_days(dictDate):
    keys = dictDate.keys()
    for key in keys:
        dateOfHolidays=dictDate[key]
        deltas = ((datetime.strptime(dateOfHolidays, '%d.%m.%y').date() - date.today()).days)
        print(f"It is {deltas} days until {key}")

dirname = os.path.dirname(__file__)
src_relative = os.path.join(dirname, 'holidays.txt')
str_from_file = read_file(src_relative)
dict = data_convert_to_dict(str_from_file)
return_count_days(dict)
from datetime import date, datetime
import os

def read_file(src_relative):
    return open(src_relative, 'r')


def data_convert_to_dict(str_from_file):
    dict = {}
    for line in str_from_file:
        date = line.strip().split(',')
        dict[date[0]]=date[1]  
    return dict    


def return_count_days(dict):
    keys = dict.keys()
    for key in keys:
        dateOfHolidays=dict[key]
        deltas = ((datetime.strptime(dateOfHolidays, '%d.%m.%y').date() - date.today()).days)
        print(f"It is {deltas} days until {key}")

dirname = os.path.dirname(__file__)
src_relative = os.path.join(dirname, 'holidays.txt')
str_from_file = read_file(src_relative)
dict = data_convert_to_dict(str_from_file)
return_count_days(dict)
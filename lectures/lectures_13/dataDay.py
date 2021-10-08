from datetime import date, datetime

def read_file(f):
    f = [line.split(',')[:] for line in f]
    return f


def take_date_and_event(f):
    event = []
    event_data_string = []
    for event_lst in f:
        print(event_lst)
        event.append(event_lst[0])
        event_data_string.append(event_lst[1])
        print(event) 
        print(event_data_string) 
    return print(f"{event} \n {event_data_string}")


print(read_file(open('E:\\Hillel\\GitHub\\py_courses\\lectures\\lectures_13\\text.txt', 'r'))

#take_date_and_event()

#def h_days(event_data_string):
  #  time_to_event = datetime.strptime(str(event_data_string), '%d.%m.%y').date() - date.today()
  #  print(time_to_event)
  #  return print(time_to_event)
  # d = date.today()
  #    print(d)
 # f = open('E:\\Hillel\\GitHub\\py_courses\\lectures\\lectures_13\\text.txt', 'r')
 
#take_date_and_event(f) 
#read_file_date(open('E:\\Hillel\\GitHub\\py_courses\\lectures\\lectures_13\\text.txt', 'r'))
#h_days(read_file_event(open('E:\\Hillel\\GitHub\\py_courses\\lectures\\lectures_13\\text.txt', 'r')))
#f = open('E:\\Hillel\\GitHub\\py_courses\\lectures\\lectures_13\\text.txt', 'r')
#print(f'It is {time_to_event} days until {read_file_event(f)}') 
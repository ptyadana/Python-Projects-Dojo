import datetime
from array import array

print(datetime.date.today())
print(datetime.time(18,20,10))

#array
#array performance is better than list
my_arr = array('i',[1,2,3,4,5])
print(my_arr[2])
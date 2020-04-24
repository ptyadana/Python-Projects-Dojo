#print the script in the expected output
# Today is Wednesday, December 28, 2016
# Hint: http://strftime.org/

# Answer:
import datetime
print(datetime.datetime.now().strftime('Today is %A, %B %d, %Y '))

# Explanation:
# We're using datetime  standard module here which supplies classes to manipulate dates and times. 
# Note that datetime.now()  would produce 2016-12-25 22:54:34.153209 which is a datetime  object. 
# However, by applying strftime (string from time) we convert that object to a readable string using format codes. 
# For example, %A  would extract the day, %B  the month, %d  the date, and %Y  the year. 
# You can find the complete list of format codes in the strftime.org website.
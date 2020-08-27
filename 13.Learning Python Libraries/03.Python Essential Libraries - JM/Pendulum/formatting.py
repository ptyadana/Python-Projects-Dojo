# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
import pendulum

# create a datetime and print it
dt1 = pendulum.datetime(2020, 7, 28, 15, 30)
print(dt1)

# use some formatting functions
print(dt1.to_date_string())
print(dt1.to_time_string())
print(dt1.to_datetime_string())


# use functions for nice formatting
print()
print(dt1.to_formatted_date_string())
print(dt1.to_day_datetime_string())


# use some common formats
print()
print(dt1.to_cookie_string())
print(dt1.to_iso8601_string())
print(dt1.to_rfc1036_string())


# use the format function for pretty printing
print()
print(dt1.format("YYYY MM-DD HH:MM:SS A"))
print(dt1.format("dddd DD MMMM YYYY"))

# use localization
print(dt1.format("dddd DD MMMM YYYY", locale="de"))
print(dt1.format("dddd DD MMMM YYYY", locale="fr"))

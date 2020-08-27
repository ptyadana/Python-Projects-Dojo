# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
import pendulum

# create some base datetimes
dt1 = pendulum.datetime(2020, 7, 28, 23, 0, 0)
dt2 = pendulum.datetime(2020, 12, 22)
print("--- Original Dates ---")
print(dt1.to_date_string())
print(dt2.to_date_string())
print("------\n")


# add and subtract various values
new_date = dt1.add(hours=1)
print(new_date.to_date_string())

new_date2 = dt1.add(minutes=60)
print(new_date2.to_date_string())

dt1 = dt1.add(years=2, months=3)
print(dt1.to_date_string())

dt1 = dt1.subtract(months=48, hours=72)
print(dt1.to_date_string())

# negative values also work
dt1 = dt1.add(years=-1)
print(dt1.to_date_string())


# Try comparing datetimes
print(dt1.is_past())
print(dt1.is_future())
print(dt1.is_leap_year())
print(dt1.is_dst())  # day light saving

print(dt1.to_date_string())
print(dt2.to_date_string())
print(dt1 > dt2)
print(dt1 < dt2)

dt3 = pendulum.datetime(2020, 12, 22)
print(dt3.to_date_string())
print(dt2 == dt3)

# Create a Period using difference
dt1 = pendulum.datetime(2020, 7, 28)
period = dt1.diff(dt2)

print(period.in_hours())
print(period.in_days())
print(period.in_months())

period = dt1.diff_for_humans(dt2)
print(period)

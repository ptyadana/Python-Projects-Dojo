import pendulum


def calculate_date(date_name, input_date):
    """tell user when is that specific date whether the date went by or coming in x days.

    Args:
        date_name (string): Name of the date (example: Korra Birthday)
        input_date (string): date string in "day<space>month" (example: 30 12)
    """
    try:
        st_day, st_month = input_date.split(" ")
        now = pendulum.today()
        
        input_date = pendulum.datetime(year=now.year, month=int(st_month), day=int(st_day))
        
        print("Today is", now.format("dddd, MMMM Do"))
        print(date_name, "is", input_date.format("dddd, MMMM Do"))

        period = input_date.diff(now)
        
        if input_date.is_past():
            print(date_name, "went by", period.in_days(), "days ago")
            input_date = input_date.add(years=1)
            
        next_year_date = input_date - now
        print("It's", next_year_date.days, "days until", date_name)
    
    except Exception as e:
        print("Invalid input. Please enter the valid date as DD<space>MM.")
        
        
if __name__ == "__main__":
    calculate_date("Korra birthday", "10 5")
    print()
    calculate_date("Christmas", "25 12")
    
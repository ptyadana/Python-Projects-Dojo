print("Welcome..")

while True:
    try:
       age = int(input("What is your age? "))
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter the age higher than zero.")
    else:
        print("Thank you.")
        break

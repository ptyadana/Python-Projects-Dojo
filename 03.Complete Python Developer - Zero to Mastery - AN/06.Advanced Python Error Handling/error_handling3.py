print("Welcome....")

while True:
    try:
       age = int(input("What is your age? "))
       age / 0
       raise ZeroDivisionError("Yo Yo customed error !!!")

    except ValueError:
        print("Please enter a number")
        break
    else:
        print("Thank you.")
        break
    finally:
        print("finally.")

def add(num1=0, num2=0):
    try:
        if num1 and num2:
            return int(num1) + int(num2)
        elif num1 == 0 or num2 == 0:
            return int(num1) + int(num2)
        else:
            return "Please enter numbers."
    except ValueError as err:
        return err
    
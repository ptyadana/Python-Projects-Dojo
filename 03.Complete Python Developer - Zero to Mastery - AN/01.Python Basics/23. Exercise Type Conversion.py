from datetime import datetime

birth_year = input("what year were you born?")
current_year = datetime.now().year
print(type(current_year))

age = current_year - int(birth_year)
print(f"Your age is {age}")
print("----- Welcome to Password Checker -----")
username = input("Enter your username: ")
password = input ("Enter your password: ")
length = len(password)
masked_password = "*" * int(length)

print(f"hi {username}, your password {masked_password} is {length} characters long.")
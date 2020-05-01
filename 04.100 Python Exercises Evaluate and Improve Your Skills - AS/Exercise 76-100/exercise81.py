#a script that lets the user to submit a password unitl they have
# satisfied three conditions:
# 1. Password contains at least one number
# 2. contains one uppercase letter
# 3. it is at least 5 chars long
# Give exact reason why the user has not created a correct password
# before asking for password, ask for username

#Answer:
print('*** Welcome to Account creation ***')

while True:
    username = input('Enter your username: ')
    with open('users.txt', mode='rt') as file:
        users = file.readlines()
        users = [user.strip('\n') for user in users]
        if username.lower() in users:
            print('Username is already existed.')
        else:
            print('Username is fine.')
            break

while True:
    password = input('Enter your password: ')
    conditions = "Password need to include "
    if len(password) < 5:
        conditions += "\n - at least 5 chars long"
    if not any(i.isdigit() for i in password):
        conditions += '\n - at least one number'
    if not any(i.isupper() for i in password):
        conditions += '\n - one upper letter'
    
    if len(conditions) > len("Password need to include "):
        print(conditions)
    else:
        print("Your password is fine.")
        break
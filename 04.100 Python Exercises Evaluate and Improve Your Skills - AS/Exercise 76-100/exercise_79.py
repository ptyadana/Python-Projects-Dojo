#create a script that lets user submit a password until they have satisifed three conditions.
#1) Password contains at least one number
#2) Contains one upper letter
#3) It is at least 5 chars long
# Print out message 'password is not fine' if the user didn't create a correctly satisfied password

# Answer (using regex):
import re
pattern = '(?=.*[0-9])(?=.*[A-Z])([a-zA-Z0-9!@#$%^&*()?]+){5,}'

user_password = input('Enter your password to check condition: ')

match = re.search(pattern, user_password)
if match:
    print('Your password satisfy the conditions. Good Job !')
else:
    print('password is not fine.')



# Answer 2: 

while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")

# Explanation:
# We're using a while  loop here because we need to keep the program running until the user submits a password that satisfies all three conditions. Line 3 contains the three conditions connected with an and  operator. Line 3 becomes True  only when all three conditions are True . If that happens, Password is fine  is generated, and the break  statement will break the loop, and the program will stop. If at least one of the conditions in Line 3 is False , Line 3 evaluates to False  and the print  statement under else is executed and the loop starts over again.
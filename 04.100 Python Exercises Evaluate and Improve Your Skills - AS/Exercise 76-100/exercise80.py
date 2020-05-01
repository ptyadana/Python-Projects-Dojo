# Create a program that asks the user to enter a new password and 
# check that the submitted password should contain 
# at least one number, 
# one uppercase letter and 
# at least 5 characters. 
# If the conditions are met,  print out the reason 
# why pointing to the specific condition/s that has not been satisfied.

#Answer 1:
while True:
    password = input('Enter your password : ')
    conditions = ["Password should contain"]
    if len(password) < 5:
        conditions.append('at least least 5 characters')
    if not any(i.isdigit() for i in password):
        conditions.append('at least one number')
    if not any(i.isupper() for i in password):
        conditions.append('at  least one upper letter')
    
    if len(conditions) > 1:
        result = " ".join(conditions)
        print(result)
    else:
        print("Your password is fine.")
        break



# Answer2: 

while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)


# Explanation:
# Again, we're using a while loop. In the first if  condition we check if there is 
# any number in the submitted password and if there is we append a message string to the notes  list. 
# Then, we check the next conditions in the next two if  conditionals and keep adding messages to notes .
#  We also check if the length of notes  is zero, because it if is that means there were no message 
# added there which means the password is fine. Lastly, under else , we iterate through 
# the constructed list and print out its items (i.e messages).

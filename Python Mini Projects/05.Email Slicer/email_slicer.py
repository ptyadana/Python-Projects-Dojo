print('***** Welcome to Simple Email Slicer *****')
email = input('Please enter your email address: ').strip()

#test@gmail.com
username = email[:email.find('@')]
domain = email[email.find('@') + 1 :email.find('.')]

print(f'\nHere is your username: {username}')
print(f'Your email domain is {domain}')
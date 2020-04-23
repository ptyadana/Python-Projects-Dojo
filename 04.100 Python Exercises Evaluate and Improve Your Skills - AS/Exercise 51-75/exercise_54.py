# Question: Please update the dictionary by changing the last name of the second employee 
# from Smith to Smooth or to whatever takes your fancy.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

# Expected output: 

# d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                 {"firstName": "Anna", "lastName": "Smooth"},
#                 {"firstName": "Peter", "lastName": "Jones"}],
# "owners":[{"firstName": "Jack", "lastName": "Petter"},
#           {"firstName": "Jessy", "lastName": "Petter"}]}

# Answer:
d['employees'][1]['lastName']='Smooth'
print(d)

# Explanation:
# On the left side of the assignment operator we are accessing Smith  as we did in the previous exercise. Then using the assignment operator we simply assign a new string to that item.
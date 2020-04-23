# Question: Please add a new employee to the dictionary.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

# Expected output: 

# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'},
#                {'firstName': 'Albert', 'lastName': 'Bert'}],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}

# Answer
new_emp = dict(firstName='Richard',lastName='Aung')
emp_list = d['employees']
emp_list.append(new_emp)

d['employees']=emp_list
print(d)

Answer2: 
d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))

# Explanation:
# d['employees']  returns this list:

# [{"firstName": "John", "lastName": "Doe"},
#  {"firstName": "Anna", "lastName": "Smith"},
#  {"firstName": "Peter", "lastName": "Jones"}]
# Then d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))  appends a new item to the list. This item happens to be a new dictionary.
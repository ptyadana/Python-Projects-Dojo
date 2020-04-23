# Question: Please download the file in the attachment and use Python to print out its content.

# Expected output: 

# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'}],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}


# Answer
import json
with open('./output/output_56.json','r') as file:
    content = json.loads(file.read())

print(content)

# Explanation:
# We're opening the file in read mode and then using json.loads  which gets a string as output and creates a dictionary object out of that.
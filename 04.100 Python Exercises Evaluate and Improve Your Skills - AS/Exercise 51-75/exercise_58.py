# Question: Please download the json file in the attachment and use Python to add a new employee to the content of the file so that the file looks like in the expected output below.

# Expected output: json file added employees_58.png

# Answer:
import json
with open('./output/output_56.json','r') as file:
    content_dict = json.loads(file.read())

content_dict['employees'].append(dict(firstname='Albert',lastname='Bert'))
print(content_dict)
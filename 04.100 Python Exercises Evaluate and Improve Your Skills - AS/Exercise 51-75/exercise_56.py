# Question: Store the dictionary in a json file.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

# Answer
import json
json_string = json.dumps(d, indent=4)

with open('./output/output_56.json','w') as file:
    file.write(json_string)

# Explanation:
# As you can see we created the json file using the standard file handling method, but then we used json.dump  which makes it easy to write the dictionary content to the file. The argument indent=4  will create 4 white spaces to indent the different levels of the dictionary items.
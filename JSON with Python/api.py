import json
from urllib.request import urlopen

with urlopen("http://dummy.restapiexample.com/api/v1/employees") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data,indent=2))

#len of the data
# print(len(data['data']))

employee = dict()

for item in data["data"]:
    name = item["employee_name"]
    salary = item["employee_salary"]
    
    employee[name] = salary

print(employee)
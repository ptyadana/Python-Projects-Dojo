import json

people_string ='''
{
    "people":[
        {
            "name":"John-Smith",
            "phone":"123-456-789",
            "emails":["john@test.com","smith@gmail.com"],
            "has_license":false
        },
         {
            "name":"Doey Timberlake",
            "phone":"444-555-666",
            "emails":null,
            "has_license":true
        }
    ]
}
'''

#load string into object
data = json.loads(people_string)

# print(type(data['people']))
# print(data)


for person in data["people"]:
    del person["phone"] #delete phone keys and values

new_string = json.dumps(data, indent=2)

print(new_string)
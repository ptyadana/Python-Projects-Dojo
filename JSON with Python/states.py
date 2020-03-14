import json

with open("states.json") as f:
    #load the file content into object
    data = json.load(f)

for state in data['states']:
    #remove area-code element
    del state['area_codes']


# new_string = json.dumps(data,indent=2)
# print(new_string)

with open('new_states.json','w') as f:
    json.dump(data, f, indent=2)
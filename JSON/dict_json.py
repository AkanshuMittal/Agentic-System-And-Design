import json 

data = {
    "Name": "John",
    "Age": 30,
    "City": "New York",
    "active_status": True
}

json_string = json.dumps(data)

print(json_string)

## Writing to a JSON file

with open("config.json", "w") as file:
    json.dump(data, file)
    

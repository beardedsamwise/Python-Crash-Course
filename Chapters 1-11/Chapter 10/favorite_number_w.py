import json

message = "Enter your favorite number: "
number = input(message)
filename = 'favorite_number.json'

with open(filename, 'w') as file_obj:
    json.dump(number, file_obj) 
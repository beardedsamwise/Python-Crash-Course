import json

filename = 'favorite_number.json'

with open(filename) as file_obj:
    number = json.load(file_obj)

print('Your favorite number is: ' + str(number))

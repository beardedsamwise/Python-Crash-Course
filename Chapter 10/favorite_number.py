import json

filename = 'favorite_number.json'
message = "Enter your favorite number: "

try:
    with open(filename) as file_obj:
        number = json.load(file_obj)
    print('Your favorite number is: ' + str(number))

except FileNotFoundError:
    number = input(message)
    with open(filename, 'w') as file_obj:
        json.dump(number, file_obj) 
    print('Your favorite number ' + str(number) + 
    ' has been saved to a JSON file')
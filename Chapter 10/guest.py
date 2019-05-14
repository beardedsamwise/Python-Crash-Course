message = "Please enter your name: "
filename = 'guest.txt'

log_text = input(message)

with open (filename, 'w') as file_object:
	file_object.write(log_text)


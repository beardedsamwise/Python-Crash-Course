message = "To quit this program enter 'q'."
message += "\nWhy do you like programming?: "

filename = 'programming.txt'

while True:
	log_text = input(message)
	if log_text == "q":
		break
	else:
		with open (filename, 'a') as file_object:
			file_object.write(log_text + '\n')
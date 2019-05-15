message = "To quit this program enter 'q'."
message += "\nPlease enter your name: "

filename = 'guest_book.txt'

while True:
	log_text = input(message)
	if log_text == "q":
		break
	else:
		with open (filename, 'w') as file_object:
			file_object.write(log_text + '\n')



current_users = ['peter','alex','john','steve','dave']

new_users = ['ralph','Alex','michael','stewart','reginald']

#finish this off
current_users_lower = []

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print("This username " + new_user + " is not available")
	else:
		print("The username " + new_user + " is available")
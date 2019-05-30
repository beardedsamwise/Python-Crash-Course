current_users = ['peter','alex','john','steve','dave']

new_users = ['Ralph','Alex','Michael','Stewart','Reginald']

#finish this off
current_users_lower = []

for users in current_users:
	current_users_lower.append(users.lower())

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print("This username " + new_user + " is not available")
	else:
		print("The username " + new_user + " is available")
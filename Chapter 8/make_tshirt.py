def make_shirt(size='large',message='I Love Python'):
	print("You have ordered a " + size.lower() + " shirt.")
	print("Your shirt has this message printed on it: " + message + "\n")

make_shirt()
make_shirt('medium')
make_shirt(message='w00t',size='x-large')
def make_shirt(size,message):
	print("You have ordered a " + size.lower() + " shirt.")
	print("Your shirt has this message printed on it: " + message.title() + "\n")

make_shirt('large','epic winrar')
make_shirt(size='medium',message='pwned')
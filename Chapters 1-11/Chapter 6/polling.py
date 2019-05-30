favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

to_poll = ['jen','peter','sarah','phil','ben']

for name, language in favorite_languages.items():
    if name in to_poll:
    	print("Thanks for taking the poll " + name.title() + "!")
    elif name not in to_poll:
    	print("Don't be lazy " + name.title() + "! Please take the poll!")
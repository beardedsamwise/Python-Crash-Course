files = ['cats.txt','dogs.txt']

for file in files:
    try:
        with open(file) as file_object:
            content = file_object.read()
        print('The contents of ' + file +  ' are:\n' + content.rstrip() + '\n')

    except FileNotFoundError:
        #print("\nDoh! The file " + file + " wasn't found!")
        pass



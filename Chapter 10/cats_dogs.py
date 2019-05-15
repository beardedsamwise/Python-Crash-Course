files = ['cats.txt','dogs2.txt']

for file in files:
    try:
        with open(file) as file_object:
            content = file_object.read()
        print(content.rstrip())

    except FileNotFoundError:
        print("doh file isn't here")




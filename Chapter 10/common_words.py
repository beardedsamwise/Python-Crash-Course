files = ['doriangrey.txt','drjekyll_mrhyde.txt']
word = 'was'

for file in files:

    word = word.lower()

    try:
        with open(file) as file_object:
            content = file_object.read()
            total_count = content.count(word)
        print('The word "' + word + '" appears ' + str(total_count) + ' times '+
        'in ' + file + '.')

    except FileNotFoundError:
        print("\nDoh! The file " + file + " wasn't found!")




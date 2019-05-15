print('This program will divide two numbers by each other and display' + 
' the result. \nIt will also catch any errors if you enter a string instead' +
    ' of an integer.\n')
while True:
    number1 = input('Enter the first number: ')
    number2 = input('Enter the second number: ')
    try:
        number1 = int(number1)
        number2 = int(number2)

        result = number1 / number2
        result = str(result)

        print('The results are in!: ' + result) 

    except ValueError:
        print('You entered a string instead of an integer!')
    
    keep_going = input('Would you like to divide more numbers (y/n)?: ')

    if keep_going == 'n':
        break
    elif keep_going == 'y':
        print('You want to continue! Great!\n')
    else:
        print("You didn't enter 'y' or 'n' so we're going to keep going!\n")



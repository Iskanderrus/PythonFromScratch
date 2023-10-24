while True:

    try:
        num_1 = float(input('Please provide first number: ').replace(',', '.'))
        num_2 = float(input('Please provide second number to add: ').replace(',', '.'))

    except ValueError:
        print('Please provide a numeric value.')

    else:
        print(f'{num_1} + {num_2} equals {round(num_1 + num_2, 3)}')
        
        if input('To continue enter "y", to exit hit any key ').lower().strip() != 'y':
            break

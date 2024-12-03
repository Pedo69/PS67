a = {'milk': '50', 'bag': '100'}

# Convert the string values to integers and add them
milk_value = int(a['milk']) + int(a['bag'])

# Get the amount the user is paying
try:
    price = int(input('Enter how much you are paying: '))
    pay_back = price - milk_value

    # Print the transaction details
    print(f'Your product price: {milk_value}, you paid: {price}, your change: {pay_back}')
except ValueError:
    print("Invalid input. Please enter a valid number for the payment.")
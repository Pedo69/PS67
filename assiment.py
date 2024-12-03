print('***calculate sum of odd and even number (Exit press 0)***')
odd = 0
even = 0
while True:
    a = int(input('Enter you number:'))


    if a % 2 == 0:
        even += a
        

    elif a % 2 != 0:
        odd += a
       
    
    if a == 0:
        print(f'sum of even number = {even}')
        print(f'sum of odd number = {odd}')
        break


    
sum = 0
while True:
    first_num = int(input('Enter you first number:'))
    last_num = int(input('Enter you last number:'))
    a = int(input('Enter you divide number'))
    for i in range(first_num + 1, last_num):
        if i % a == 0:
            sum = i
            print(f'result is {sum}')

    repeat = input('You want to try again? exit press 0, continue press1:').strip().lower()
    if repeat == '0':
        print('End programe')
        break
    elif repeat == '1':
         continue
    
    
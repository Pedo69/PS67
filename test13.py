first_num = int(input('Enter you first number:'))
last_num = int(input('Enter you last number:'))

sum = 0
for i in range(first_num + 1, last_num):
    if i % 3 == 0:
        sum = i
        print(f'you count from {first_num} to {last_num} is {sum}')

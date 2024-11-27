import random
print('***welcome to the number gussing game***')
print("i'm think of a number between 1 and 100. can you guss it? ")
max = 5
guss_count = 0
secrect_number = random.randint(0,101)
print(secrect_number)


while True:
    guss = int(input('Enter you number:'))
    guss_count += 1

    if guss == secrect_number:
        print(f'you win and you round is {guss_count}')
        break
    elif guss > secrect_number:
        print('too height')
    elif guss < secrect_number:
        print('too low')

    if guss_count != max:
        continue
    else:
        print('i sus')
        break





loan = int(input('Enter you loan count:'))

if loan <= 1000:
    interest = 0.1
elif loan >= 10000:
    interest = 0.05
else:
    interest = 0.02

result = (loan + (loan * interest))
print(f'you payment is: {result}')
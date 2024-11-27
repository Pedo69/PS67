print('***calculate the sum between strat and stop number***')
a = int(input('Enter you start number:'))
b = int(input('Enter you stop number:'))
sum = 0
for i in range(a, b + 1):
    sum = sum + i
print(f'the sum from {a} to {b} {sum}')
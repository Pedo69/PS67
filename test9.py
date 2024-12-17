print('*****calculate saraly*****')
worker_count = int(input('Enter you count:'))

for i in range(worker_count):
    pay_rate = int(input('Enter you pay rate:'))
    hour = int(input('Enter you work hour:'))

    if hour <= 160:
        saraly = pay_rate * hour
    else:
        saraly = (pay_rate * 160) + ((hour - 160) * 1.5 * pay_rate)
    print(f'worker count {i+1}: saraly: {saraly:.2f}')
print(f'Total number of worker: {worker_count}')
print('*****End programe*****')
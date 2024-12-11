pay_rate = int(input('Enter you pay rate:'))
hour = int(input('Enter you work hour:'))

if hour <= 160:
    saraly = pay_rate * hour
    print(saraly)
else:
    saraly = (pay_rate * 160) + ((hour - 160) * 1.5 * pay_rate)
    print(saraly)
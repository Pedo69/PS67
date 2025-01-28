y = int(input('Enter you money:'))
b = int(input('1.ดอนล่า 2.ยูโร:'))

if b == 1:
    price = y // 33.83
else:
    price = y // 35

print(f'you thai bath {y} you change {price:.2f}')
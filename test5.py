print('***convert BMI***')
a = int(input('Enter you weight (kg): '))
b = int(input('Enter you height (m):'))

bmi = a / (b ** 2)
print(f'you BMI is : {bmi: .5f}')

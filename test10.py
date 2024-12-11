student_num = int(input('Enter your student count: '))

for i in range(student_num):
    score = int(input(f'Enter score for student {i+1}: ')) 
    
    if score >= 80:
        print('A')
    elif score >= 70:
        print('B')
    elif score >= 60:
        print('C')
    elif score >= 50:
        print('D')
    else:
        print('F')

print(f'Total number of students: {student_num}')

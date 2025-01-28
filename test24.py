student_count = int(input('Enter your student count: '))
students = []
for i in range(student_count):
    name = input('Enter your name: ')
    score = input('Enter your score: ')
    students.append((name, score))
print(f'Student count: {student_count}')
for student in students:
    print(f'Name: {student[0]}, Score: {student[1]}')

 
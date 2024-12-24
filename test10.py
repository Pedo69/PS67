import time
student_num = int(input('Enter your student count: '))
start = time.time()
for i in range(student_num):
    score = int(input(f'Enter score for student {i+1}: ')) 
    
    if score >= 80:
        grade = 'A'
    elif score >= 75:
        grade = 'B+'
    elif score >= 70:
        grade = 'B'
    elif score >= 65:
        grade = 'C+'
    elif score >= 60:
        grade = 'C'
    elif score >= 55:
        grade = 'D+'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print(f'student number {i+1} grade {grade}')
print(f'Time taken: { (time.time()-start) * 1000:.2f} ms')
print(f'Total number of students: {student_num}')

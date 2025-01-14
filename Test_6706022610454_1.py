brun = 0
day = int(input('Number of exercise days: '))
while True:
    for i in range(day):
        print(f'--------day {i+1}----------')
        hour = int(input('Give time to exercise (minute):'))    
        ty  = int(input('Select exercise type 1.Running 2.Cycling 3.Swimming: '))

        if ty > 3:
            print('There are only 3 options')
            break
        if ty == 1:
            cal = 10 * hour
            brun += cal
            print(f'Run brun cal {cal}')
        elif ty == 2:
            cal = 8 * hour
            brun += cal
            print(f'cycling brun cal {cal}')
        else:
            cal = 5 * hour
            brun += cal
            print(f'swimming brun cal {cal}')
        print('-----------------------')

    print(f'Number of exercise days: {day} burn calories: {brun}')
           
    repeat = input('You want to try again? exit press 0, continue press1:').strip().lower()
    if repeat == '0':
        print('End programe')
        break



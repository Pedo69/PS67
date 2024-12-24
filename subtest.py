target_money = int(input('จำนวนเงินที่ออม:'))
year= int(input('จำนวนปีที่ออม:'))
ch = int(input('คุณต้องการออมเงินเเบบไหน \n 1 รายวัน: \n 2 รายเดือน:'))
if ch == 1:
    day = (year * 365) 
    result = target_money / day
    print(f'จำนวนวัน {day} วัน จำนวนเงินออม: {result:.2f}')
elif ch == 2:
    day = (year * 12) 
    result = (target_money / day)
    print(f'จำนวนวัน {day} เดือน จำนวนเงินออม: {result:.2f}')
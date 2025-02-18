#นาย สุธินันท์ ครองแถว 6706022610349
#นาย ธราธิป ศลิปานุรักษ์ 6706022610411
#นาย อภิชา เภาอ่อน 6706022610454

print('This program is Collect information about provinces in various regions of Thailand')
print('Menu\n 1.InsertData\n 2.UpdateData\n 3.SearchData\n 4.DeleteData\n 5.ViewAllData \n')
Thai_dict = dict(
    ภาคเหนือ = ['เชียงราย', 'เชียงใหม่'],
    ภาคกลาง = ['พิษณุโลก', 'สุโขทัย'],
    ภาคตะวันออกเฉียงเหนือ = ['หนองคาย', 'นครพนม'],
    ภาคตะวันออก = ['ชลบุรี', 'ระยอง'],
    ภาคตะวันตก = ['กาญจนบุรี', 'ราชบุรี'],
    ภาคใต้ = ['สงขลา', 'กระบี่'],
)

while True:
    chosen = input('Plesase select menu:')

    # 1.InsertData
    if chosen == '1':
        region = input('Enter region: ')
        if region in Thai_dict:
            province = input('Enter province: ')
            if province not in Thai_dict[region]:
                Thai_dict[region].append(province)
                print('Province added successfully')
            else:
                print('Province already exists in this region.')
        else:
            print('Region not found')

    # 2.UpdateData
    elif chosen == '2':
        region = input('Enter region:')
        if region in Thai_dict:
            province = input('Enter province:')
            Thai_dict[region] = province
            print('UpdateData successfully')
        else:
            print('Region not found')

    # 3.SearchData
    elif chosen == '3':
        region = input('Enter region:')
        if region in Thai_dict:
            print(Thai_dict[region])
        else:
            print('Region not found')

    # 4.DeleteData
    elif chosen == '4':
        region = input('Enter region:')
        if region in Thai_dict:
            Thai_dict.pop(region)
            print('Region deleted successfully')
        else:
            print('Region not found')

    #5.viewAllData        
    elif chosen == '5':
        print(Thai_dict)

    else:
        print('Invalid menu')
        break
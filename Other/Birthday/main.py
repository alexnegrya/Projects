from dates import *

while True:
    clear()
    print('Введите дату в формате ДД.ММ.ГГГГ (например 01.январь.2000)')
    data = input('\n>>> ')
    error('Дата введена в неправильном формате!')
    continue
    try:
        spl = data.split('.')
        _day = int(spl[0])
        _month = spl[1]
        for i in range(1, 13):
            if _month == months[i]:
                _month_number = i
        _year = int(spl[2])
        if _year in range(1900, year):
            if _year % 400 == 0:
                leap = True
            elif _year % 4 == 0:
                leap = True
            elif _year % 100 != 0:
                leap = False
            if leap and _month == 2:
                if _day in range(1, 30):
                    user = PersonBirthday(_day, _month, _year)
                else:
                    error(f'Такой даты не существует!')
                    continue
            elif leap == False and _month == 2:
                if _day in range(1, 29):
                    user = PersonBirthday(_day, _month, _year)
                else:
                    error(f'Такой даты не существует!')
                    continue
            else:
                if _month % 2 == 0:
                    if _day in range(1, 32):
                        user = PersonBirthday(_day, _month, _year)
                    else:
                        error(f'Такой даты не существует!')
                        continue
                else:
                    if _day in range(1, 31):
                        user = PersonBirthday(_day, _month, _year)
                    else:
                        error(f'Такой даты не существует!')
                        continue
        else:
            error(f'Поддерживаются года с 1900, меньше текущего года, введен {_year} год!')
            continue
    except:
        error('Дата введена в неправильном формате!')
        continue
    further = None
    while further != '' or further != 'заново':
        clear()
        print(f"Введена дата {user}")
        print('\nНажмите ENTER чтобы продолжить,')
        print('или введите \"заново\" чтобы повторно ввести дату')
        further = input('\n>>> ')
        if further == 'заново':
            back = True
            break
        else:
            back = False
            break
    if back:
        continue

from data import *

while True:
    clear()

    # Сокращение колличества жизней
    if snowman in mines:
        if m_1 == True:
            if snowman == mine_1:
                coord = mine_1.get_coord()
                mine_1.del_coord(gm, '')
                m_1 = False
        if m_2 == True:
            if snowman == mine_2:
                coord = mine_2.get_coord()
                mine_2.del_coord(gm, '')
                m_2 = False
        if m_3 == True:
            if snowman == mine_3:
                coord = mine_3.get_coord()
                mine_3.del_coord(gm, '')
                m_3 = False
        snowman.set_hp(op='sub')
        snowman.set_coord(gm, y=coord[0], x=coord[1])
    hp = snowman.get_hp()
    if hp == 0:
        clear()
        sleep(0.01)
        print(f'{skull.get()} Вы проиграли!')
        break

    # Вывод колличества жизней
    print_hp(snowman)
    print()

    # Вывод карты
    for y in range(len(gm)):
        for x in range(len(gm[y])):
            if gm[y][x] == 1:
                print(character.get(), end=' ')
            elif gm[y][x] == 2:
                print(mine.get(), end=' ')
            elif gm[y][x] == 3:
                print(mine.get(), end=' ')
            elif gm[y][x] == 4:
                print(mine.get(), end=' ')
            else:
                print(land.get(), end=' ')
        print()

    # Интерактивность
    enter = option.action()
    if enter == 'a':
        snowman.del_coord(gm)
        snowman.set_coord(gm, direction='влево')
    elif enter == 'd':
        snowman.del_coord(gm)
        snowman.set_coord(gm, direction='вправо')
    elif enter == 'w':
        snowman.del_coord(gm)
        snowman.set_coord(gm, direction='вверх')
    elif enter == 's':
        snowman.del_coord(gm)
        snowman.set_coord(gm, direction='вниз')
    elif enter in ru:
        print(f'\n{cross.get()} Вводите буквы на английском чтобы все работало!')
        clear('')
    elif enter in ('выход', 'exit', 'quit'):
        clear()
        print('Спасибо за игру!')
        break

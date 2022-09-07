from os import system
# a - move left
# d - move right

lenght = 20
roboX = 5
alienX_1 = 10
alienX_2 = 15
alienX_3 = 2
hearts = 3
gift_heartX_1 = 13
gift_heartX_2 = 3
pistolX = 17
pistol = False
score = 0

print('Сollect 200 score points to win')

while True:
    system('cls')

    # ########### DRAWING THE MAP ##############
    x = 1
    print('\n')

    # limits
    if roboX == 21:
        roboX = 1
    if roboX == 0:
        roboX = 20

    # gift hearts
    if roboX == gift_heartX_1 or roboX == gift_heartX_2:
        if roboX == gift_heartX_1:
            gift_heartX_1 -= 30
            score += 50
        if roboX == gift_heartX_2:
            gift_heartX_2 -= 30
            score += 50
        hearts += 1

    # hp
    if roboX == alienX_1 or roboX == alienX_2 or roboX == alienX_3:
        hearts -= 1
        if hearts == 0:
            print('Game over!')
            break
    if hearts > 0 and score < 200:
        print('❤ ' * hearts)
    
    # pistol
    if roboX == pistolX:
        score += 50
        pistol = True
        pistolX -= 30
    if pistol == True:
        print('🔫')
    
    # score
    if hearts > 0 and score < 200:
        print('Score:',score)
    else:
        print('Congratulations! You win!')
        break

    # drawing
    for x in range(1,21):
        if x == roboX:
            print('🤖', end = '')
        elif x == alienX_1 or x == alienX_2 or x == alienX_3:
            print('👾', end = '')
        elif x == gift_heartX_1 or x == gift_heartX_2:
            print('💟', end = '')
        elif x == pistolX:
            print('🔫', end = '')
        else:
            print('-', end = '')
        x += 1

    print('\n')
    # ##########################################

    # ############### CONTROLS #################
    if pistol == True:
        direction = input('a/d/f l/f r/x > ')
    else:
        direction = input('a/d/x > ')
    if direction == 'f l' or direction == 'f r' and pistol == True:
        fire_l = roboX - 1
        fire_r = roboX + 1
    if direction == 'f l' and pistol == True:
        if fire_l == alienX_1 or fire_l == alienX_2 or fire_l == alienX_3:
            if fire_l == alienX_1:
                alienX_1 -= 30
            if fire_l == alienX_2:
                alienX_2 -= 30
            if fire_l == alienX_3:
                alienX_3 -= 30
            score += 50
            pistol = False
    if direction == 'f r' and pistol == True:
        if fire_r == alienX_1 or fire_r == alienX_2 or fire_r == alienX_3:
            if fire_r == alienX_1:
                alienX_1 -= 30
            if fire_r == alienX_2:
                alienX_2 -= 30
            if fire_r == alienX_3:
                alienX_3 -= 30
            score += 50
            pistol = False
    if direction == 'a':
        roboX -= 1
    if direction == 'd':
        roboX += 1
    if direction == 'x':
        system('cls')
        print('Thank you for playing!')
        break
    # ##########################################

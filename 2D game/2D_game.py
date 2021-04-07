from os import system
from random import randint

# ############### HELP ################

help_controls = 'Controls:\
\n● Enter [a] - to move left\
\n● Enter [d] - to move right\
\n● Enter [w] - to move up\
\n● Enter [s] - to move down'

help_exit = 'Enter [exit] to exit the game.'

help_jump = 'Jump bonus 🡅 allows you to jump on three squares:\
\n● Leftward - if you enter [j a]\
\n● Rightward - if you enter [j d]\
\n● Upward - if you enter [j w]\
\n● Downward - if you enter [j s]'

help_win = 'Collect 300 $ to win.'

# #####################################

# ############ COORDINATES ############

# snowman
snowmanX = 5
snowmanY = 5

# mines
mine1X = 2
mine1Y = 4

mine2X = 8
mine2Y = 6

# hearts
hearts = 3

# jump bonus
jumpX = 5
jumpY = 7
jump_hp = 5
jump = False

# money
money1X = 10
money1Y = 3

money2X = 2
money2Y = 5

money3X = 7
money3Y = 7

money = 0

# swords
swordsX = randint(1, 10)
swordsY = randint(1, 10)

swords = False
swords_hp = 3

condition = False

if snowmanX == swordsX and snowmanY == swordsY:
    condition = True
elif mine1X == swordsX and mine1Y == swordsY:
    condition = True
elif mine2X == swordsX and mine2Y == swordsY:
    condition = True
elif jumpX == swordsX and jumpY == swordsY:
    condition = True
elif money1X == swordsX and money1Y == swordsY:
    condition = True
elif money2X == swordsX and money2Y == swordsY:
    condition = True
elif money3X == swordsX and money3Y == swordsY:
    condition = True

if condition == True:
    swordsX = randint(1, 10)
    swordsY = randint(1, 10)

# hint
hint = True
hint_text = '\n(Enter [help] to get information about game)'

# #####################################

while True:
    system('cls')
    print()

    # jump bonus system
    if snowmanX == jumpX and snowmanY == jumpY:
        jump = True
        jumpX -= 20
        jumpY -= 20

    if jump_hp == 0:
        jump = False

    # swords bonus
    if snowmanX == swordsX and snowmanY == swordsY:
        swordsX -= 20
        swordsY -= 20
        swords = True
    
    if swords_hp == 0:
        swords = False

    # hp -
    if snowmanX == mine1X and snowmanY == mine1Y:
        hearts -= 1
    elif snowmanX == mine2X and snowmanY == mine2Y:
        hearts -= 1

    # money
    if snowmanX == money1X and snowmanY == money1Y:
        money += 100
        money1X -= 20
        money1Y -= 20
    elif snowmanX == money2X and snowmanY == money2Y:
        money += 100
        money2X -= 20
        money2Y -= 20
    elif snowmanX == money3X and snowmanY == money3Y:
        money += 100
        money3X -= 20
        money3Y -= 20

    # game panel
    if swords == True and hearts > 0 and jump == True and money < 300:
        print('❤ ' * hearts,' Money: ',money,'$\n',' 🡅 ',jump_hp, '⚔ ', swords_hp)
    elif swords == True and hearts > 0 and money < 300:
        print('❤ ' * hearts, ' Money: ' ,money, '$\n', '⚔ ', swords_hp)
    elif hearts > 0 and jump == True and money < 300:
        print('❤ ' * hearts, ' Money: ', money, '$\n', ' 🡅 ', jump_hp)
    elif hearts > 0 and money < 300:
        print('❤ ' * hearts,' Money: ',money,'$\n')

    # limits
    if snowmanX > 10:
        snowmanX = 10
    elif snowmanX < 1:
        snowmanX = 1
    elif snowmanY > 10:
        snowmanY = 10
    elif snowmanY < 1:
        snowmanY = 1

    # win
    if money == 300:
        print('Congratulations! You win!')
        break

    # game over
    if hearts == 0:
        print('Game over!')
        break

    # #################### Y loop #####################
    for y in range(1,11):

        # #################### X loop #####################
        for x in range(1,11):
            if snowmanX == x and snowmanY == y:
                print("⛇ ", end="")
            elif mine1X == x and mine1Y == y:
                print('☠ ', end='')
            elif mine2X == x and mine2Y == y:
                print('☠ ', end='')
            elif jumpX == x and jumpY == y:
                print('🡅 ', end='')
            elif swordsX == x and swordsY == y:
                print('⚔ ', end='')
            elif money1X == x and money1Y == y:
                print('$ ', end='')
            elif money2X == x and money2Y == y:
                print('$ ', end='')
            elif money3X == x and money3Y == y:
                print('$ ', end='')
            else:
                print("◼ ", end="")
        # #################### X loop #####################
        print()
    # #################### Y loop #####################

    # hint
    if hint == True:
        print(hint_text)
        hint = False

    # ################# CONTROLS ######################

    # user input
    enter = input('\n> ')

    # simple controls
    if enter == 'a':
        snowmanX -= 1
    elif enter == 'd':
        snowmanX += 1
    elif enter == 'w':
        snowmanY -= 1
    elif enter == 's':
        snowmanY += 1

    # jump bonus controls
    if jump == True:
        if enter == 'j a':
            snowmanX -= 3
            jump_hp -= 1
        elif enter == 'j d':
            snowmanX += 3
            jump_hp -= 1
        elif enter == 'j w':
            snowmanY -= 3
            jump_hp -= 1
        elif enter == 'j s':
            snowmanY += 3
            jump_hp -= 1
    
    # swords bonus controls
    if swords == True:
        if enter == 's a':
            n = snowmanX - 1
            if n == mine1X and mine1Y == snowmanY:
                mine1X -= 20
                mine1Y -= 20
            elif n == mine2X and mine2Y == snowmanY:
                mine2X -= 20
                mine2Y -= 20
            swords_hp -= 1
        elif enter == 's d':
            n = snowmanX + 1
            if n == mine1X and mine1Y == snowmanY:
                mine1X -= 20
                mine1Y -= 20
            elif n == mine2X and mine2Y == snowmanY:
                mine2X -= 20
                mine2Y -= 20
            swords_hp -= 1
        elif enter == 's w':
            n = snowmanY - 1
            if mine1X == snowmanX and n == mine1Y:
                mine1X -= 20
                mine1Y -= 20
            elif mine2X == snowmanX and n == mine2Y:
                mine2X -= 20
                mine2Y -= 20
            swords_hp -= 1
        elif enter == 's s':
            n = snowmanY + 1
            if mine1X == snowmanX and n == mine1Y:
                mine1X -= 20
                mine1Y -= 20
            elif mine2X == snowmanX and n == mine2Y:
                mine2X -= 20
                mine2Y -= 20
            swords_hp -= 1
                

    # help
    if enter == 'help':
        system('cls')
        h = input('Enter a number of help topic:\
        \n1) Controls\
        \n2) How to exit the game\
        \n3) Jump bonus\
        \n4) How to win\
        \n\n> '               )
        if h == '1':
            system('cls')
            print(help_controls)
        elif h == '2':
            system('cls')
            print(help_exit)
        elif h == '3':
            system('cls')
            print(help_jump)
        elif h == '4':
            system('cls')
            print(help_win)
        input('\nPress [Enter] to continue game > ')

    # exit the game
    if enter == 'exit':
        system('cls')
        print('\nThank you for playing!')
        break

    # #################################################
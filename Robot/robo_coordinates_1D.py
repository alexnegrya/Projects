lenght = int(input('Enter lenght: '))
roboX = int(input('Enter robot coordinates: '))

x = 1
print('\n')
while x <= lenght:
    if roboX < 1 or roboX > lenght:
        roboX = 1
        print('You do not pass!')
    if x == roboX:
        print('R', end = '')
    else:
        print('-', end = '')
    x += 1
print('\n')

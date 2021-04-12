def drawLine(lenght, direction):
    if direction == 'h':
        print('-' * lenght)
    elif direction == 'v':
        print('|\n' * lenght)

drawLine(5, 'h')

print()

drawLine(3, 'v')

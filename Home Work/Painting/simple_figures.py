figure = input("What figure to draw? ")

if figure == "line":
    print("-----"),
elif figure == 'square':
    print('-----')
    print('|   |')
    print('|   |')
    print('-----'),
elif figure == 'parallel horizontal lines':
    print('-----')
    print('-----'),
elif figure == 'parallel vertical lines':
    print('|   |')
    print('|   |'),
else:
    print("CAN'T DRAW SUCH FIGURE!")  
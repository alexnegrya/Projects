#   * * * # # * * * # # * * * # #

n1 = [4, 9, 14]
n2 = [5, 10, 15]

for x in range(16):
    if x in n1:
        print('# ', end='')
    elif x in n2:
        print('# ', end='')
    else:
        print('* ', end='')

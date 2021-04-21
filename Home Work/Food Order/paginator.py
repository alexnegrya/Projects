from os import system
from math import ceil

def paginator(l, b, title=None):

    # help
    h = 'Print [<] or [>] to go to the previous or next page\
or [p] to go the specified page\nand [back] to go back to menu'

    # hint
    hint = True

    # paginator data
    per_page = 5
    current_page = 1
    page_total = ceil(len(l) / per_page)
    page_min = (len(l)) - (len(l)) + 1

    while True:

        start_i = (current_page - 1) * per_page
        end_i = start_i + per_page

        if title != None:
            # print list
            print(f'{title}:\n')
            for i in range(len(l)):
                if i in range(start_i, end_i):
                    print(l[i])
            print()

        # print pages
        for page in range(1, page_total + 1):
            if page == current_page:
                print(f'[{page}]', end=' ')
            else:
                print(page, end=' ')
        print()

        # interaction
        if hint == True:
            print('Print [help] to more information')
            hint = False
        print()

        enter = input('>>> ')
        system('clear')

        if enter == 'p':
            print('Enter the number of the page you want to go')
            choose = int(input('\n>>> '))
            if choose < page_min:
                current_page = page_min
            elif choose > page_total:
                current_page = page_total
            else:
                current_page = choose
            system('clear')
        elif enter == '<':
            current_page -= 1
            if current_page < page_min:
                current_page = 1
        elif enter == '>':
            current_page += 1
            if current_page > page_total:
                current_page = page_total
        elif enter == 'help':
            system('clear')
            print(h)
            input('\nPress [enter] to continue... ')
            system('clear')
        elif enter == 'back':
            p = True
            return p
        break

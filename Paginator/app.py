from os import system
from math import ceil

l = [
    'Jacob',
    'Alvin',
    'Abel',
    'Dennis',
    'Donald',
    'Kelly',
    'Christopher',
    'Steven',
    'John',
    'Aldous',
    'Samuel',
    'Curtis',
    'Winfred',
    'Christopher',
    'Peter'
]

# help
h = 'Print [<] or [>] to go to the previous or next page\
and [p] to go the specified page'

# hint
hint = True

# paginator data
per_page = 5
current_page = 1
page_total = ceil(len(l) / per_page)
page_min = (len(l)) - (len(l)) + 1

while True:
    system('clear')

    start_i = (current_page - 1) * per_page
    end_i = start_i + per_page

    # print list
    print('List:\n')
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
    enter = input('\n>>> ')
    print()

    if enter == 'p':
        print('Enter the number of the page you want to go')
        choose = int(input('\n>>> '))
        if not choose < page_min or not choose > len(l):
            current_page = choose
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
    elif enter == 'exit':
        system('clear')
        break

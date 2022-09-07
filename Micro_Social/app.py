from data import users
from math import ceil
from os import system

# menu
print('Menu:\n')
menu = { 1: '1) Print list of users' }
for n in range(20):
    if n in menu: print( menu[n] )
print()

option = input('\nChoose option > ')

per_page = 5
current_page = 1
page_total = ceil(len(users) / per_page)
page_min = (len(users)) - (len(users)) + 1

while True:
    system('clear')

    start_i = (current_page - 1) * per_page
    end_i = start_i + per_page

    if option == '1':
        print( '\nList of users:\n' )
        for i in range( len(users) ):
            if i in range(start_i, end_i):
                name = users[i]['name']
                city = users[i]['adress']['city']

                status = '●' if users[i]['online'] else '○'

                print( f'> {name:18} (  {city:9} ) {status}' )
        print('-' * 20)

    for page in range(1, page_total + 1):
        if page == current_page: 
            print('[', page, ']', end=' ')
        else:
            print(page, end=' ')
    print()

    print('Enter [p] to choose page or < > to navigate in list or [exit]\n')
    enter = input('>>> ')
    print()
    if enter == 'p':
        print('Enter the number of the page you want to go to')
        choose = int(input('\n>>> '))
        if not choose < page_min or not choose > len(users):
            current_page = choose
    elif enter == '<':
        current_page -= 1
        if current_page < page_min: current_page = 1
    elif enter == '>':
        current_page += 1
        if current_page > page_total: current_page = page_total
    elif enter == 'exit':
        system('clear')
        break

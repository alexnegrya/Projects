from os import system
from paginator import *


def wait(): input('\nPress ENTER to continue... ')

def sure(item, quantity):
    system('clear')
    print(f"Are you sure what you want to order «{item}» x{quantity}?")
    choose = input('\n(Yes/No) >>> ')
    return 'Yes' if choose == 'Yes' else 'No'

back = False
def print_items( items, title = None, total = None):
    def print_title():
        if title != None:
            print("#"*38)
            print(title)
        print("#"*38)

    from app import order
    from app import food

    system('clear')
    value = 'avail' if items == food else 'quantity'

    if len(items) != 0:
        while True:
            print_title()
            for i in range(len(items)):
                print(f"{i + 1}) {items[i]['name']:6} x{items[i][value]:3}\
                {items[i]['price']['amount']:4} {items[i]['price']['currency']}"
            )
            if total: print(order['total']['amount'],
                order['total']['currency'])
            print("#" * 38)
            input()
            break
    else:
        print("#" * 38 + '\n')
        print('\nHere will be food what you ordered\n')
        print("#" * 38 + '\n')

def print_actions_menu(items, title=None):
    system("clear")
    if title != None:
        print("#"*20)
        print(title)
    print("#"*20)
    for i in range(len(items)):
        print(f"{i+1} {items[i]:15}")
    print("#"*20)
    return int(input(">>> "))


def create_order_item(food, item_i, item_q):
    return {
        "name": food[item_i]['name'],
        "quantity": item_q,
        "price": {
            "amount": item_q * food[item_i]['price']['amount'],
            "currency": "MDL"
        }
    }

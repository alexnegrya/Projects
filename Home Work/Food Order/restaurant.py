from os import system
from paginator import *

def wait():
    input('\nPress ENTER to continue... ')

def sure(item, quantity):
    system('clear')
    print(f"Are you sure what you want to order «{item}» x{quantity}?")
    choose = input('\n(Yes/No) >>> ')
    if choose == 'Yes':
        return 'Yes'
    else:
        return 'No'

back = False
def printItems( items, title = None, total = None):
    from app import order
    system('clear')
    def printTitle():
        if title != None:
            print("#"*38)
            print(title)
        print("#"*38)
    from app import food
    if items == food:
        value = 'avail'
    else:
        value = 'quantity'
    if len(items) != 0:
        while True:
            printTitle()
            for i in range(len(items)):
                print( 
                f"{i+1}) {items[i]['name']:6} x{items[i][value]:3}\
                {items[i]['price']['amount']:4} {items[i]['price']['currency']}"
            )
            if total == True:
                print(order['total']['amount'], order['total']['currency'])
            print("#"*38)
            pg = paginator(items, back)
            if pg == True:
                break
    else:
        print("#"*38+'\n')
        print('\nHere will be food what you ordered\n')
        print("#"*38+'\n')

def printActionsMenu(items, title=None):
    system("clear")
    if title != None:
        print("#"*20)
        print(title)
    print("#"*20)
    for i in range(len(items)):
        print(
            f"{i+1} {items[i]:15}"
        )
    print("#"*20)
    
    opt = int(input(">>> "))
    return opt


def createOrderItem(food, item_i, item_q):
    return {
        "name": food[item_i]['name'],
        "quantity": item_q,
        "price": {
            "amount": item_q * food[item_i]['price']['amount'],
            "currency": "MDL"
        }
    }

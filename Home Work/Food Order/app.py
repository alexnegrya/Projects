from db import *
from restaurant import *

# data
food = load('food')
order = {
    "items": [],
    'total': {
        'amount': 0,
        'currency': 'MDL'
    },
    'client': {
        'name': {
            'first': '',
            'last': ''
        },
        'adress': {
            'country': '',
            'city': ''
        },
        'phone': '',
        },
    'delivery': {
        'amount': 0,
        'currency': 'MDL'
    }
}

while True:
    action = printActionsMenu(
        [
            "Show food",
            "Order food",
            "Show order",
            'Checkout',
            "Exit"
        ],
        "MAIN MENU"
    )
    
    if action == 1:
        printItems( food, "TODAYS MENU" )
    
    if action == 2:
        # input order data
        item_i = int(input("Which item? ")) - 1 # index
        item_q = int(
            input(f"How many «{food[item_i]['name']}» do you want? ")
        )

        # check, confirmation, update data
        if item_q <= 0:
            print(f"Error: Order at least one «{food[item_i]['name']}»!")
            wait()
        elif item_q <= food[item_i]['avail'] and item_q > 0:
            s = sure(food[item_i]['name'], item_q)
            if s == 'Yes':
                new_item = createOrderItem(food, item_i, item_q)
                order["items"].append(
                    new_item
                )
                order['total']['amount'] += new_item['price']['amount']
                food[item_i]['avail'] -= item_q
                save('food', food)
                print(
                    f"«{food[item_i]['name']}» x{item_q} was successfully added to the order!")
                wait()
        else:
            print(
                f"Error: This quantity of «{food[item_i]['name']}» is not available!")
            wait()

    if action == 3:
        printItems( order["items"], "YOUR ORDER", True)
        wait()
    
    if action == 4:
        data = []
        # name
        name = input('Enter your full name: ')
        data.append(name)
        for i in data:
            spl = i.split()
            order['client']['name']['first'] = spl[0]
            order['client']['name']['last'] = spl[1]
        data.clear()
        
        # adress
        adress = input('Enter your country and city: ')
        data.append(adress)
        for i in data:
            spl = i.split()
            order['client']['adress']['country'] = spl[0]
            order['client']['adress']['city'] = spl[1]
        data.clear()

        # phone number
        phone = input('Enter your phone number: ')
        order['client']['phone'] = phone

        # delivery
        print('Do you need delivery?')
        delivery = input('(Yes/No) >>> ')
        if delivery == 'Yes' and order['total']['amount'] < 200:
            order['delivery']['amount'] = 100
            order['total']['amount'] += 100

            # bill
            print('Successfully! You cheque:\n')
            billPrint(order)
            billSave('bill', order)
            wait()
        
    if action == 5:
        break
    
# После завершения процесса оформления заказа - вывести красиво (форматированно)\
#  - чек на экран И тот же чек сохранить в простой текстовый файл с названием "bill.txt" в папку data


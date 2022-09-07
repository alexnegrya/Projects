from os import system

# data
clients = ["John", "Marry", "Kate"]

clientsHighPriority = ["Tob", "Pete"]
clientsLowPriority = ["Vicky", "Lessly"]

# wait function
def wait(clear=False):
    input('\nPress ENTER to continue... ')
    if clear == True:
        system('clear')

# print clients list function
def showClients(listName, title=None):
    if title != None:
        print(f"{title}:\n")
    for c in range(len(listName)):
        print(f"{c+1}. {listName[c]}")

# add clients
re_enter = False
back = False
error = False

while True:
    name = input('Enter your name: ')
    add = input('Set your priority (High/Low): ')
    if add == 'High':
        clientsHighPriority.insert(0, name)
        print('\nYour name has been successfully added to start of the client list!')
        wait(True)
    elif add == 'Low':
        clientsLowPriority.append(name)
        print('\nYour name has been successfully added to end of the client list!')
        wait(True)
    else:
        system('clear')
        print('Error: You entered incorrect data!\n')
        while True:
            print('Do you want to re-enter data?\n')
            do = input('(Yes/No) >>> ')
            if do == 'Yes':
                re_enter = True
                break
            elif do == 'No':
                back = True
                error = True
                break
            system('clear')
    if re_enter == True:
        system('clear')
        re_enter = False
        continue
    if back == True:
        break
    options = ['Add another one cliet', 'Exit and print client list']
    print('What do you want to do next?\n')
    for p in range(len(options)):
        print(f"{p+1}) {options[p]}")
        if p == len(options):
            print()
    enter = int(input('>>> '))
    if enter == 1:
        system('clear')
        continue
    elif enter == 2:
        break

# add high priority clients to start of clients list
clientsHighPriority.reverse()
for high in range(len(clientsHighPriority)):
    clients.insert(0, clientsHighPriority[high])

# add low priority clients to end of clients list
for low in range(len(clientsLowPriority)):
    clients.append(clientsLowPriority[low])

# print clients list
if error != True:
    system('clear')
    showClients(clients, 'Clients')

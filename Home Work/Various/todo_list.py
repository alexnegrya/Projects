from os import system

# ########### data ############
tasks = []

n = 0
# #############################

while True:
    # ########## interaction ###############
    print('--- Menu ---')
    menu = print('1. Add new task\
    \n2. Show tasks\
    \n3. Remove task\
    \n4. Clear TODO list\
    \n5. Clear programm\
    \n0. Exit')
    choice = input('\n> ')
    print()

    if choice == '1':
        new_task = input('Add new task: ')
        if new_task not in tasks:
            tasks.append(new_task)
            print('\nTask was added succesfully!')
        else:
            print('\nThis task is alredy exits!')
        print()
    elif choice == '2':
        print('TODO list: (', len(tasks), ') :')
        for i in range(len(tasks)):
            n = i + 1
            print(n, '>', tasks[i])
        print()
    elif choice == '3':
        remove = int(input('Print the number of task what you want to remove: '))
        remove -= 1
        tasks.pop(remove)
        print('\nTask was removed succesfully!')
        print()
    elif choice == '4':
        tasks.clear()
        print('TODO list was cleared succesfully!')
        print()
    elif choice == '5':
        system('cls')
        print('Programm was cleared succesfully')
        print()
    elif choice == '0':
        print('You are sure what you want to exit?\n')
        s = input('Yes or No: ')
        if s == 'Yes': 
            system('cls')
            print()
            break
        else:
            print()
    # ######################################

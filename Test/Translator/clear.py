from os import system

def clear(wait=None):
    if wait != None:
        input('\nPress ENTER to continue...')
        system('clear')
    else:
        system('clear')
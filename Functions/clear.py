from os import system

def clear(wait=None):
    if wait == None:
        system('clear')
    elif wait != None:
        input('\nНажмите Enter чтобы продолжить... ')
        system('clear')

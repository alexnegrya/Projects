import requests
from os import system


# Get user ip address, then country code
def getCode():
    url = 'https://freegeoip.app/json/'
    res = requests.get(url)
    data = res.json()
    if len(data) == 1: raise SystemExit(data['message'])
    c = data['country_code']
    return c

def wait(): input('\nContinue... ')

def clr(): system('clear')


while True:
    print(
        '1) Print all holidays\
        \n2) Search holidays by name or letter(s)\
        \n3) Exit'
    )
    option = input('\n>>> ')

    if option == '1' or option == '2':
        year = input('\nYear: ')

        print('Waiting for a server response... ')
        res = requests.get(f"https://date.nager.at/api/v2/PublicHolidays/{year}/{getCode()}")
        data = res.json()
        clr()

    if option == '1':
        for i in range(len(data)):
            print(f"{i + 1}) {data[i]['name']}")
    elif option == '2':
        search = input('Enter name or letter(s): ')
        for i in range(len(data)):
            result = []
            if search in data[i]['name']:
                result.append(data[i]['name'])
                print(f"{i + 1}) {data[i]['name']}")
                if len(result) == 0:
                    print('Nothing found')
    elif option == '3':
        clr()
        print('Thanks you for using my app!')
        break
    else:
        print('Choose correct option!')
    wait()
    clr()

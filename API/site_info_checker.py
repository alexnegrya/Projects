import requests
from os import system


if __name__ != '__main__': print('This module works only separately')


domain = input('Enter domain: ')
print('\nWait...\n')
url = requests.get(f'http://ip-api.com/json/{domain}')
system('clear')

data = url.json()

if data['status'] == 'success' and domain != '':
    print(f'Domain "{domain}" was found successfully!\n')
    print(f"Physical address: {data['country']}, {data['city']}")
    print(f"IP address: {data['query']}")
    print(f"Company name: {data['org']}")
elif domain == '': print('Error: you not entered domain!')
else: print(f'Error: Domain "{domain}" not found!')

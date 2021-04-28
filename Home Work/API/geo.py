import requests
from os import system

query = input('Enter domain: ')

print('\nWait...\n')
url = requests.get(f'http://ip-api.com/json/{query}')
system('clear')

data = url.json()

if data['status'] == 'success' and query != '':
    print(f'Domain <{query}> was found successfully!\n')
    input('Press ENTER to see domain info... ')
    system('clear')

    print(f"Domain adress: {data['country']}, {data['city']}")
    print(f"Domain ip adress: {data['query']}")
    print(f"Domain company name: {data['org']}")
elif query == '':
    print('Error: you not entered domain!')
else:
    print(f'Error: Domain <{query}> not found!')
print()

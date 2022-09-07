from os import system
import platform

try:
    import requests
    from pycountry import countries
except ModuleNotFoundError as e:
    i = str(e).find("'")
    print('Please install', "".join([char for char in str(e)[i:] \
        if char != "'"]))


SYSTEM = platform.system()

def clear_terminal():
    if SYSTEM in ('Linux', 'Darwin'): system('clear')
    elif SYSTEM == 'Windows': system('cls')

def degree_to_direction_mapper(deg: int):
    """
    Accepts wind degree as integer number and returns wind direction string.
    """
    if deg in range(0, 90): middle, directions = 90 / 2, (
        'North ⬆', 'Northeast ⬈')
    elif deg in range(90, 180): middle, directions = (180 + 90) / 2, (
        'East ➡', 'Southeast ⬊')
    elif deg in range(180, 270): middle, directions = (270 + 180) / 2, (
        'South ⬇', 'Southwest ⬋')
    elif deg in range(270, 0): middle, directions = (360 + 270) / 2, (
        'West ⬅', 'Northwest ⬉')
    return directions[0 if deg < middle else 1]


KEY = '38e7180f4c8c4cf17d3a635f0000dad1' # openweathermap.org key
URL = f"https://api.openweathermap.org/data/2.5/weather"
PARAMS = {'q': input('Enter a city: '), 'appid': KEY, 'units': 'metric'}

print('Waiting for response...\n')
data = requests.get(URL, PARAMS).json()
clear_terminal()

if data['cod'] == 200:
    # input(data)
    country_code = data['sys']['country']
    country_name = countries.get(alpha_2=country_code).name
    print('-' * 30, f"{data['name']}, {country_name} ({country_code})",
        '-' * 30)
    print(f"Weather: {data['weather'][0]['main']}")
    print(f"Temperature: {data['main']['temp']} ℃ ,",
        f"Feels like: {data['main']['feels_like']} ℃")
    print(f"Wind speed: {data['wind']['speed']} km/h")
    print(f"Wind direction: {degree_to_direction_mapper(data['wind']['deg'])}")
else:
    print(f'Error {data["cod"]}: {data["message"]}!')

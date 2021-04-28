import requests

# wind degree to direction
def degreeToDirectionMapper(deg):
    # North
    if deg in range(0, 90):
        middle = 90 / 2
        if deg < middle:
            direction = 'North ⬆'
        elif deg >= middle:
            direction = 'Northeast ⬈'
    
    # East
    elif deg in range(90, 180):
        middle = (180 + 90) / 2
        if deg < middle:
            direction = 'East ➡'
        elif deg >= middle:
            direction = 'Southeast ⬊'

    # South
    elif deg in range(180, 270):
        middle = (270 + 180) / 2
        if deg < middle:
            direction = 'South ⬇'
        elif deg >= middle:
            direction = 'Southwest ⬋'

    # West
    elif deg in range(270, 0):
        middle = (360 + 270) / 2
        if deg < middle:
            direction = 'West ⬅'
        elif deg >= middle:
            direction = 'Northwest ⬉'
    return direction

# openweathermap.org
key = '38e7180f4c8c4cf17d3a635f0000dad1'

city = input('Enter a city: ')

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

print('Waiting for response...\n')
res = requests.get(url)
data = res.json()

if data['cod'] == 200:
    print('-'*20, f"{data['name']}, {data['sys']['country']}", '-'*20)
    print(f"Weather: {data['weather'][0]['main']}")
    print(
        f"Temperature: {data['main']['temp']} ℃ , Feels like: {data['main']['feels_like']} ℃")
    print(f"Wind speed: {data['wind']['speed']} km/h")
    print(f"Wind direction: {degreeToDirectionMapper(data['wind']['deg'])}")
    print()
else:
    print(f'Error {data["cod"]}: {data["message"]}!')

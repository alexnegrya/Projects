# Решение
def season(month_number):
    if month_number in range(0, 4):
        return 'Зима'
    elif month_number in range(4, 7):
        return 'Весна'
    elif month_number in range(7, 10):
        return 'Лето'
    elif month_number in range(10, 13):
        return 'Осень'

# Проверка
print(season(2))

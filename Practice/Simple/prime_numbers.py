# Решение
def is_prime(number):
    if number in range(0, 1001):
        if number % 2 == 0:
            return True
        else:
            return False

# Проверка
print(is_prime(5))
print(is_prime(10))

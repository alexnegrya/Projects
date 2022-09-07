def hi(lang, name):
    if lang == 'en':
        print(f'Hello, {name}!')
    elif lang == 'ru':
        print(f'Привет, {name}!')
    elif lang == 'ro':
        print(f'Salut, {name}!')
    else:
        print(f'Error: language "{lang}" is not recongrized!')


if __name__ == '__main__':
    hi('en', 'Sarah')
    hi('ru', 'Иван')
    hi('ro', 'Ion')
    hi('ge', 'Kolya')

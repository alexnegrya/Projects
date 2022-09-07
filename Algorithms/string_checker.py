# This algorythm-function check whether the string contains:
# 1) Only same letters (example: "aaa")
# 2) Numbers (example: "john01")

import re


def check_str(string: str) -> None:
    # Collecting charss repetitions counts
    repeatitions_counts = {char: len(re.findall(char, string)) \
        for char in string}
    # Checking for the same chars only
    for i in range(len(repeatitions_counts)):
        if repeatitions_counts[string[i]] == len(string): raise ValueError(
            'the string contains only the same letters')
    # Cheking for numbers
    if any([char.isnumeric() for char in string]): raise ValueError(
        'the string must not contain integer values')


if __name__ == '__main__':
    msg = 'String is correct'
    try: check_str(input('Enter string for check >>> '))
    except ValueError as e: msg = str(e)[0].upper() + str(e)[1:]
    raise SystemExit(msg)

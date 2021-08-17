# This algorythm-function check whether the string contains:
# 1) Only same letters (example: "aaa")
# 2) Numbers (example: "john01")

def str_check(string):
    # Spliting name by letters
    splited = []
    for i in range(len(string)):
        splited.append(string[i])

    # Checking name for letters repition
    repeat_numbers = {}
    for i in range(len(splited)):
        if splited[i] not in repeat_numbers:
            repeat_numbers[splited[i]] = 1
        else:
            repeat_numbers[splited[i]] += 1

    # Checking name for the same letters only
    for i in range(len(repeat_numbers)):
        if repeat_numbers[splited[i]] == len(name):
            raise NameError('the name contains only the same letters')

    # Cheking name for numbers
    contains_numbers = False
    for value in splited:
        try:
            int(value)
            raise NameError('the name must not contain integer values')
        except ValueError:
            pass

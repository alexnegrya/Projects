def is_type(t, variable):
    if type(t) == str:
        if t == 'str':
            if type(variable) == str:
                return True
            else:
                return False
        elif t == 'int':
            if type(variable) == int:
                return True
            else:
                return False
        elif t == 'float':
            if type(variable) == float:
                return True
            else:
                return False
        else:
            print('Неизвестный тип данных!')
    else:
        print('Проверяемый тип данных указан в неверном формате!')

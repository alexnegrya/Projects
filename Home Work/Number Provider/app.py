from NumberProvider import NumberProvider

def positiveAction(number):
    print("Got an positive number >>>", number)

def negativeAction(number):
    print('Got an negative number >>>', number)

provider = NumberProvider()
provider.whenPositive(positiveAction)
provider.whenNegative(negativeAction)
provider.start()

# Ответы:
# AttributeError - ошибка в аргументе, отсутсвует positiveCB
# Ошибка исчезла потому что в метод whenPositive была передана функция positiveAction

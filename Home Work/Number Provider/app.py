from NumberProvider import NumberProvider

def positiveAction(number):
    print("Got an positive number >>>", number)

def negativeAction(number):
    print('Got an negative number >>>', number)

provider = NumberProvider()
provider.whenPositive(positiveAction)
provider.whenNegative(negativeAction)
provider.start()
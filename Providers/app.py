from numbers_providers import NumbersProvider


def positive_action(number):
    print("Got a positive number >>>", number)

def negative_action(number):
    print('Got a negative number >>>', number)


if __name__ == '__main__':
    provider = NumbersProvider(positive_action, negative_action)
    provider.start()

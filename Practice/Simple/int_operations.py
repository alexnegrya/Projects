import unittest

# Решение
def arithmetic(num_1, num_2, operation):
    if operation == '+':
        return num_1 + num_2
    elif operation == '-':
        return num_1 - num_2
    elif operation == '*':
        return num_1 * num_2
    elif operation == '/':
        return num_1 / num_2
    else:
        return 'Неизвестная операция'


# Проверка
class ArithmeticTestCase(unittest.TestCase):

    def test_plus(self):

        self.assertEqual(arithmetic(3, 4, '+'), 7)

    def test_minus(self):

        self.assertEqual(arithmetic(3, 4, '-'), -1)

    def test_multiply(self):

        self.assertEqual(arithmetic(3, 4, '*'), 12)

    def test_divide(self):

        self.assertEqual(arithmetic(3, 4, '/'), 3/4)

    def test_unknown(self):

        self.assertEqual(arithmetic(3, 4, '.'), "Неизвестная операция")


if __name__ == "__main__":
    unittest.main()

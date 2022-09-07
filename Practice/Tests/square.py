from math import sqrt
import unittest


# Решение
def get_square_data(square_side):
    perimeter = square_side * 4
    square = square_side ** 2
    diagonal = sqrt(2) * square_side
    return (perimeter, square, diagonal)


# Проверка
class SquareTestCase(unittest.TestCase):
    def test_square(self):
        for a in range(10):
            with self.subTest(a=a):
                self.assertCountEqual(
                    # Избегаем проблемы с числами с плавающей точкой
                    list(map(lambda x: round(x, 7), get_square_data(a))),
                    list(map(lambda x: round(x, 7), [4*a, a**2, a*sqrt(2)])))


if __name__ == "__main__":
    unittest.main()

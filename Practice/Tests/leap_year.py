import unittest

# Решение
def is_year_leap(year):
    if year % 4 != 0: return False
    elif year % 100 == 0:
        return year % 400 == 0
    else: return True

# Проверка
class YearTestCase(unittest.TestCase):
    def test_year_leap(self):
        for year in (2000, 2016, 1916):
            with self.subTest(year=year):
                self.assertTrue(is_year_leap(year),
                                "{} на самом деле високосный".format(year))

    def test_year_notleap(self):
        for year in (1900, 2014, 2001):
            with self.subTest(year=year):
                self.assertFalse(is_year_leap(year),
                                 "{} на самом деле не високосный".format(year))


if __name__ == "__main__":
    unittest.main()

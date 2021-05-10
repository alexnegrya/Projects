import unittest

# Решение
def date(day, month, year):
    # Проверка на високосный год
    if year % 4 != 0:
        leap = False
    elif year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
    
    # Проверка правильности месяца и установка колличества дней
    months_high = [1, 3, 5, 7, 8, 10, 12]
    months_low = [4, 6, 9, 11]
    if month in range(1, 13):
        if month in months_high:
            days = 31
        elif month == 2:
            if leap == True:
                days = 29
            elif leap == False:
                days = 28
        elif month in months_low:
            days = 30
    else:
        return False
    
    # Проверка существования числа дня и возврат результата
    if day in range(1, days + 1):
        return True
    else:
        return False

# Проверка
class DateTestCase(unittest.TestCase):

    def test_leap_years(self):

        for year in (2000, 2016, 1916):
            with self.subTest(year=year):
                self.assertTrue(date(29, 2, year),
                                "{} високосный".format(year))

        for year in (1900, 2014, 2001):
            with self.subTest(year=year):
                self.assertFalse(date(29, 2, year),
                                 "{} не високосный".format(year))

    def test_valid_dates(self):

        self.assertTrue(date(1, 1, 1900))
        self.assertTrue(date(28, 2, 1900))
        self.assertTrue(date(1, 1, 1))
        self.assertTrue(date(31, 1, 2000))
        self.assertTrue(date(31, 12, 1900))

    def test_invalid_month(self):

        self.assertFalse(date(1, 13, 1900))
        self.assertFalse(date(2, 14, 2003))

    def test_invalid_day(self):

        self.assertFalse(date(32, 1, 1900))
        self.assertFalse(date(30, 2, 1900))
        self.assertFalse(date(31, 4, 1900))

    def test_invalid_all(self):

        self.assertFalse(date(32, 13, 1900))


if __name__ == "__main__":
    unittest.main()

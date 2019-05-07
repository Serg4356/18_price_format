import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):

    def test_incorrect_object_type_inputted(self):
        price = format_price({1: 2, 3: 4})
        self.assertIsNone(price)

    def test_invalid_string_literal_inputted(self):
        price = format_price('invalid_string_literal')
        self.assertIsNone(price)

    def test_number_without_decimal_part_if_int(self):
        price = format_price('12345.00')
        self.assertEqual(price, '12 345')

    def test_number_with_decimal_part_if_float(self):
        price = format_price('12345.45')
        self.assertEqual(price, '12 345.45')

    def test_only_two_decimal_digits(self):
        price = format_price('12345.45234234')
        self.assertEqual(price, '12 345.45')


if __name__ == '__main__':
    unittest.main()

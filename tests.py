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

    def test_integer(self):
        price = format_price(12345)
        self.assertEqual(price, '12 345')

    def test_float(self):
        price = format_price(12345.1313213)
        self.assertEqual(price, '12 345.13')

    def test_round_more_than_three_decimal_digits_almost_one(self):
        price = format_price(12345.999)
        self.assertEqual(price, '12 346')

    def test_round_more_than_three_digits_ninety_nine(self):
        price = format_price(12345.99)
        self.assertEqual(price, '12 345.99')

    def test_none(self):
        price = format_price(None)
        self.assertIsNone(price)

    def test_decimal_almost_one_cent(self):
        price = format_price(12345.0051)
        self.assertEqual(price, '12 345.01')

    def test_decimal_almost_zero(self):
        price = format_price(12345.00000000456)
        self.assertEqual(price, '12 345')

    def test_boolean(self):
        price = format_price(True)
        self.assertIsNone(price)


if __name__ == '__main__':
    unittest.main()

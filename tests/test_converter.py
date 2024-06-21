import unittest
from currency_converter import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CurrencyConverter()

    def test_direct_conversion(self):
        self.assertEqual(self.converter.convert(100, 'AUD', 'USD'), 83.71)
        self.assertEqual(self.converter.convert(100, 'USD', 'JPY'), 11995)

    def test_inverse_conversion(self):
        self.assertEqual(self.converter.convert(100, 'USD', 'AUD'), 119.46)

    def test_cross_conversion(self):
        self.assertEqual(self.converter.convert(100, 'AUD', 'JPY'), 10041)

    def test_same_currency(self):
        self.assertEqual(self.converter.convert(100, 'AUD', 'AUD'), 100)

    def test_unknown_rate(self):
        self.assertIsNone(self.converter.convert(100, 'KRW', 'FJD'))

if __name__ == '__main__':
    unittest.main()

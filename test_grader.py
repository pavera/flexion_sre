import unittest
from decimal import Decimal
from temp_converters import TempConverter

class TempTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tc = TempConverter()


class TestFarenheight(TempTestCase):

    def test_f_to_k(self):
        k = self.tc.f_to_k(32)
        self.assertEqual(k, Decimal('273.15'))

    def test_f_to_c(self):
        c = self.tc.f_to_c(32)
        self.assertEqual(c, 0)

    def test_f_to_r(self):
        r = self.tc.f_to_r(32)
        self.assertEqual(r, Decimal('491.67'))


class TestKelvin(TempTestCase):

    def test_k_to_f(self):
        f = self.tc.k_to_f(0)
        self.assertEqual(f, Decimal('-459.67'))

    def test_k_to_c(self):
        c = self.tc.k_to_c(0)
        self.assertEqual(c, Decimal('-273.15'))

    def test_k_to_r(self):
        r = self.tc.k_to_r(0)
        self.assertEqual(r, 0)


class TestCelsius(TempTestCase):

    def test_c_to_f(self):
        f = self.tc.c_to_f(0)
        self.assertEqual(f, 32)

    def test_c_to_k(self):
        k = self.tc.c_to_k(0)
        self.assertEqual(k, Decimal('273.15'))

    def test_c_to_r(self):
        r = self.tc.c_to_r(0)
        self.assertEqual(r, Decimal('491.67'))


class TestRankine(TempTestCase):

    def test_r_to_f(self):
        f = self.tc.r_to_f(0)
        self.assertEqual(f, Decimal('-459.67'))

    def test_r_to_c(self):
        c = self.tc.r_to_c(0)
        self.assertEqual(c, Decimal('-273.15'))

    def test_r_to_k(self):
        k = self.tc.r_to_k(0)
        self.assertEqual(k, 0)


class TestConversionLogic(TempTestCase):

    def test_rounding(self):
        result = self.tc.run_conversion('0', 'Celsius', 'Kelvin', '272.5')
        self.assertEqual(result, 'correct')

    def test_large_round(self):
        result = self.tc.run_conversion('0', 'Celsius', 'Kelvin', '272.6')
        self.assertEqual(result, 'correct')


if __name__ == '__main__':
    unittest.main()
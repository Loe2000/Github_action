import example
import unittest


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.addition(1, 2), 3)

    def test_sub_1(self):
        self.assertEqual(example.subtraction(8, 2), 6)

    def test_mult_1(self):
        self.assertEqual(example.multiplication(5, 6), 30)

    def test_div_1(self):
        self.assertEqual(example.division(18, 3), 6)


if __name__ == '__main__':
    unittest.main()

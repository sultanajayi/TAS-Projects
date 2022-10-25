import compare
import unittest


class TestComparison(unittest.TestCase):
    def test_string(self):
         self.assertEqual(compare.new_string("Sultan ", "Ajayi"), "Sultan Ajayi")
    def test_number(self):
         self.assertEqual(compare.new_number(2, 10), 20)

if __name__ == '__main__':
    unittest.main()

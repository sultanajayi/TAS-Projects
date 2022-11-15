import covert
import unittest


class MyTestCase(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(covert.convert('hello'), 'HELLO')


if __name__ == '__main__':
    unittest.main()

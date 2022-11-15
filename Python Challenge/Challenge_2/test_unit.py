import challenge
import unittest


class MyTestCase(unittest.TestCase):

    def test_pf(self):
        self.assertEqual(challenge.pf(3, 5), 243)


if __name__ == '__main__':
    unittest.main()

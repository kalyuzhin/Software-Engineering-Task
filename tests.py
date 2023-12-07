import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        self.assertEqual(main.print_func(), "Hello World!!")
        self.assertEqual(1 + 2, 3)
        self.assertFalse(1 + 1 == 3, "FALSE")
        self.assertEqual(len(main.print_func()), 13)


if __name__ == '__main__':
    unittest.main()

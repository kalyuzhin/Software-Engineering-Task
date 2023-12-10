import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(True, True)  # add assertion here
        self.assertEqual(main.print_func(), "Hello World!!")
        self.assertEqual(1 + 2, 3)
        self.assertFalse(1 + 1 == 3, "FALSE")
        self.assertEqual(len(main.print_func()), 13)

    def test_second(self):
        self.assertEqual(False, False)
        self.assertEqual(1, 1)
        self.assertEqual(36 ** 0.5, 6.0)
        self.assertEqual([x for x in [1, 23, 3, 544, 35, 32, 323] if x == 35], [35])

    def test_third(self):
        self.assertEqual("   Hello World!!   ".strip(), "Hello World!!")
        self.assertEqual("e" in "abcdefg", True)


if __name__ == '__main__':
    unittest.main()

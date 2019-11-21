import unittest
import book as bk


class test_book(unittest.TestCase):
    """
    Book rent shope test suite.
    """

    def setUp(self):
        pass

    def test_1_regular_type(self):
        res = bk.book_rented(books=2, booktype="regular", duration=5)
        print(res)
        self.assertEqual(res[0], 13)
        res = bk.book_rented(books=2, booktype="regular", duration=2)
        print(res)
        self.assertEqual(res[0], 4)

    def test_2_friction_type(self):
        res = bk.book_rented(books=6, booktype="friction", duration=5)
        print(res)
        self.assertEqual(res[0], 90)

    def test_3_novels_type(self):
        res = bk.book_rented(books=4, booktype="novels", duration=6)
        print(res)
        self.assertEqual(res[0], 36)
        res = bk.book_rented(books=3, booktype="novels", duration=2)
        print(res)
        self.assertEqual(res[0], 27)


if __name__ == "__main__":
    unittest.main()

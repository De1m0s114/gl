import unittest


class TestListMethods(unittest.TestCase):
    def test_Yegor_Panasuk_FI94(self):
        list=[1, 2, 3, 4, 5, 6]
        self.assertEqual(rem_last_element(list),[1, 2, 3, 4, 5])

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

if name == 'main':
    unittest.main()
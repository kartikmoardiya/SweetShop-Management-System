import unittest

class TestSweetShop(unittest.TestCase):
    def test_sort_by_name(self):
        result = self.shop.sweet_search("name")
        expected = sorted(self.sweets, key=lambda s: s.name)
        self.assertEqual(result, expected)
        

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
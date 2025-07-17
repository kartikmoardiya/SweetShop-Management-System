import unittest
from sweet import Sweet
from operations_function import SweetOperator


class TestSweetShop(unittest.TestCase):
    def setUp(self):
        self.sweets = [
            Sweet(1,"Laddu", "Indian", 10, 50),
            Sweet(2,"Barfi", "Indian", 15, 30),
            Sweet(3,"Gulab Jamun", "Indian", 12, 40),
            Sweet(4,"Brownie", "Western", 20, 20),
        ]
    
        self.shop = SweetOperator()
        self.shop.sweets = self.sweets
        
    def test_sort_by_name(self):
        result = self.shop.sweet_search("name")
        expected = sorted(self.sweets, key=lambda s: s.name)
        self.assertEqual(result, expected)
    
    def test_sort_by_category(self):
        result = self.shop.sweet_search("category")
        expected = sorted(self.sweets, key=lambda s: s.category)
        self.assertEqual(result, expected)
        
    def test_sort_by_price(self):
        result = self.shop.sweet_search("price")
        expected = sorted(self.sweets, key=lambda s: s.price)
        self.assertEqual(result, expected)
        

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
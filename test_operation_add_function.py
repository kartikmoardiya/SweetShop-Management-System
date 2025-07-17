import unittest
from operations_function import SweetOperator

class TestOperatorsAdd(unittest.TestCase):
    
    def setUp(self):
        self.addOperator =  SweetOperator()
        
    def test_add_valid_sweet(self):
        result = self.addOperator.add_sweet(
            id = 1,
            name = "Kaju Katari",
            category = "chocolate",
            price = 50,
            quantity = 10
        )
        
        self.assertEqual(result, "Sweet Added Successfully")
        self.assertEqual(len(self.addOperator.get_sweets()),1)
        
    def test_add_sweet_duplicate_id(self):
        self.addOperator.add_sweet(1,"Kaju Katli", "chocolate", 50, 10)
        self.addOperator.add_sweet(1,"Kaju Katli", "chocolate", 50, 10)
        result1  = self.addOperator.add_sweet(name="Kaju Katli", category="chocolate", price=50, quantity=10)
        result = self.addOperator.add_sweet(1, "Gulab Jamun", "candy", 40, 5)
        self.assertEqual(result, "Invalid ID")
        self.assertEqual(result1, "Invalid ID")
        
        
    def test_add_sweet_invalid_category(self):
        result1 = self.addOperator.add_sweet(id=1002, name="Barfi",price= 40, quantity=5) 
        result = self.addOperator.add_sweet(1002, "Barfi", "icecream", 40, 5)
        self.assertEqual(result, "Invalid Category")
        self.assertEqual(result1, "Invalid Category")
        
        
    def test_add_sweet_invalid_price(self):
        result1 = self.addOperator.add_sweet(id=1003, name="Rasgulla", category="candy",quantity= 5)
        result = self.addOperator.add_sweet(1003, "Rasgulla", "candy", 0, 5)
        self.assertEqual(result, "Invalid Price")
        self.assertEqual(result1, "Invalid Price")
        
        
    def test_add_sweet_invalid_quantity(self):
        result1 = self.addOperator.add_sweet(id=1004,name="Ladoo", category="pastry",price= 30)
        result = self.addOperator.add_sweet(1004, "Ladoo", "pastry", 30, -5)
        self.assertEqual(result, "Invalid Quantity")
        self.assertEqual(result1, "Invalid Quantity")
        
        
    def test_add_sweet_blank_name(self):
        result = self.addOperator.add_sweet(id=1005,category = "candy", price = 10, quantity = 5)
        self.assertEqual(result, "Invalid Name")



if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
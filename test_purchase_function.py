import unittest
from operations_function import SweetOperator

class TestSweetPurchase(unittest.TestCase):

    def setUp(self):
        self.operator = SweetOperator()
        # Add a few sweets for purchase tests
        self.operator.add_sweet(1, "Kaju Katli", "chocolate", 50, 10)
        self.operator.add_sweet(2, "Gulab Jamun", "candy", 40, 5)

    def test_purchase_successful(self):
        result = self.operator.sweet_purchase("Kaju Katli", 3)
        self.assertEqual(result, "Purchase Successful. 3 Kaju Katli(s) purchased. Remaining stock: 7")
        # Check that the quantity is updated correctly
        sweets = self.operator.view_sweets()
        for sweet in sweets:
            if sweet.name == "Kaju Katli":
                self.assertEqual(sweet.quantity, 7)
    
    def test_purchase_insufficient_stock(self):
        result = self.operator.sweet_purchase("Kaju Katli", 20)
        self.assertEqual(result, "Insufficient Stock")
        # Stock should remain unchanged
        sweets = self.operator.view_sweets()
        for sweet in sweets:
            if sweet.name == "Kaju Katli":
                self.assertEqual(sweet.quantity, 10)

    def test_purchase_invalid_quantity(self):
        result = self.operator.sweet_purchase("Kaju Katli", -5)
        self.assertEqual(result, "Invalid Purchase Quantity")
        # Quantity should remain unchanged
        for sweet in self.operator.view_sweets():
            if sweet.name == "Kaju Katli":
                self.assertEqual(sweet.quantity, 10)

    def test_purchase_sweet_not_found(self):
        result = self.operator.sweet_purchase("Rasgulla", 2)
        self.assertEqual(result, "Sweet Not Found")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
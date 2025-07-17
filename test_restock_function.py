import unittest
from operations_function import SweetOperator

class TestSweetRestock(unittest.TestCase):

    def setUp(self):
        self.operator = SweetOperator()
        # Add some sweets to the list
        self.operator.add_sweet(1, "Kaju Katli", "chocolate", 50, 10)
        self.operator.add_sweet(2, "Gulab Jamun", "candy", 40, 5)

    def test_restock_successful(self):
        result = self.operator.restock_sweets("Kaju Katli", 7)
        self.assertEqual(result, "Restock Successful. 7 Kaju Katli(s) restocked. Current stock: 17")
        # Quantity is updated
        sweets = self.operator.view_sweets()
        for sweet in sweets:
            if sweet.name == "Kaju Katli":
                self.assertEqual(sweet.quantity, 17)

    def test_restock_invalid_quantity(self):
        result = self.operator.restock_sweets("Kaju Katli", -5)
        self.assertEqual(result, "Invalid Restock Quantity")
        for sweet in self.operator.view_sweets():
            if sweet.name == "Kaju Katli":
                self.assertEqual(sweet.quantity, 10)   # Unchanged

    def test_restock_zero_quantity(self):
        result = self.operator.restock_sweets("Kaju Katli", 0)
        self.assertEqual(result, "Invalid Restock Quantity")
        for sweet in self.operator.view_sweets():
            if sweet.name == "Kaju Katli":
                self.assertEqual(sweet.quantity, 10)   # Unchanged

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
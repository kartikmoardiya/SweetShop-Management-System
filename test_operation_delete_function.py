import unittest
from operations_function import SweetOperator

class TestOperatorsDelete(unittest.TestCase):
    def setUp(self):
        self.deleteOperator = SweetOperator()
        # Adding some sweets for testing delete functionality
        self.deleteOperator.add_sweet(1, "Kaju Katli", "chocolate", 50, 10)
        self.deleteOperator.add_sweet(2, "Gulab Jamun", "candy", 40, 5)
        self.deleteOperator.add_sweet(3, "Barfi", "pastry", 30, 8)

    def test_delete_valid_sweet(self):
        result = self.deleteOperator.delete_sweets(1)
        self.assertEqual(result, "Sweet Deleted Successfully")
        self.assertEqual(len(self.deleteOperator.get_sweets()), 2)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
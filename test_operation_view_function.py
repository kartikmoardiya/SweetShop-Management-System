import unittest
from operations_function import SweetOperator

class TestOperatorsView(unittest.TestCase):

    def setUp(self):
        self.operator = SweetOperator()

    def test_view_empty_sweets(self):
        sweets = self.operator.view_sweets()
        self.assertEqual(sweets, [])   # Should be empty list when no sweets are added

    def test_view_after_adding_one_sweet(self):
        self.operator.add_sweet(1, "Kaju Katli", "chocolate", 50, 10)
        sweets = self.operator.view_sweets()
        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0].name, "Kaju Katli")
        self.assertEqual(sweets[0].category, "chocolate")
        self.assertEqual(sweets[0].price, 50)
        self.assertEqual(sweets[0].quantity, 10)

    def test_view_after_adding_one_sweet(self):
        self.operator.add_sweet(1, "Kaju Katli", "chocolate", 50, 10)
        sweets = self.operator.view_sweets()
        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0].name, "Kaju Katli")
        self.assertEqual(sweets[0].category, "chocolate")
        self.assertEqual(sweets[0].price, 50)
        self.assertEqual(sweets[0].quantity, 10)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
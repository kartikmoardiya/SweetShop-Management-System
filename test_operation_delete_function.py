import unittest

class TestOperatorsDelete(unittest.TestCase):
    def test_delete_valid_sweet(self):
        result = self.deleteOperator.delete_sweets(1)
        self.assertEqual(result, "Sweet Deleted Successfully")
        self.assertEqual(len(self.deleteOperator.get_sweets()), 2)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
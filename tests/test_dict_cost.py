# Allows for test execution without the need to be in the test folder
import sys
from pathlib import Path

parent_directory = Path(__file__).parent.resolve()
sys.path.insert(0, f"{parent_directory}/..")

# Import function to be tested
from src.dict_cost import get_cost

# Import unittest module
import unittest

class TestGetCost(unittest.TestCase):
    def test_empty_dictionary(self):
        """Test when costs dictionary is empty"""
        result = get_cost({}, [], 0.69)
        self.assertEqual(result, 0.0)

    def test_empty_items_list(self):
        """Test when items list is empty"""
        costs = {"item1": 10.0, "item2": 20.0}
        result = get_cost(costs, [], 0.69)
        self.assertEqual(result, 0.0)

    def test_normal_case(self):
        """Test with valid inputs and multiple items"""
        costs = {"item1": 10.0, "item2": 20.0, "item3": 30.0}
        items = ["item1", "item2"]
        result = get_cost(costs, items, 0.69)
        # Expected: (10 + 20) * (1 + 0.69) = 30 * 1.69 = 50.70
        self.assertEqual(result, 50.70)

    def test_items_not_in_costs(self):
        """Test when requested items are not in costs dictionary"""
        costs = {"item1": 10.0, "item2": 20.0}
        items = ["item3", "item4"]
        result = get_cost(costs, items, 0.69)
        self.assertEqual(result, 0.0)

    def test_some_items_in_costs(self):
        """Test when only some requested items are in costs dictionary"""
        costs = {"item1": 10.0, "item2": 20.0, "item3": 30.0}
        items = ["item1", "item4"]
        result = get_cost(costs, items, 0.69)
        # Expected: (10) * (1 + 0.69) = 10 * 1.69 = 16.90
        self.assertEqual(result, 16.90)

    def test_zero_tax(self):
        """Test with zero tax rate"""
        costs = {"item1": 10.0, "item2": 20.0}
        items = ["item1", "item2"]
        result = get_cost(costs, items, 0)
        self.assertEqual(result, 30.0)

    def test_negative_costs(self):
        """Test with negative costs"""
        costs = {"item1": -10.0, "item2": -20.0}
        items = ["item1", "item2"]
        result = get_cost(costs, items, 0.69)
        # Expected: (-30) * (1 + 0.69) = -30 * 1.69 = -50.70
        self.assertEqual(result, -50.70)

if __name__ == '__main__':
    unittest.main()

# Allows for test execution without the need to be in the test folder
import sys
from pathlib import Path

parent_directory = Path(__file__).parent.resolve()
sys.path.insert(0, f"{parent_directory}/..")

# Import class to be tested
from src.dict_class import MyDictionary 

# Import unittest module
import unittest

class TestDictionary(unittest.TestCase):
    def test_newentry_and_look(self):
        d = MyDictionary()
        d.newentry('Apple', 'A fruit that grows on trees')
        self.assertEqual(d.look('Apple'), 'A fruit that grows on trees')
        self.assertEqual(d.look('Banana'), "Can't find entry for Banana")

    def test_empty_dictionary(self):
        d = MyDictionary()
        self.assertEqual(d.look('Anything'), "Can't find entry for Anything")

if __name__ == "__main__":
    unittest.main()

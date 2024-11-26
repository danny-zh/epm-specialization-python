# Allows for test execution without the need to be in the test folder
import sys
from pathlib import Path

parent_directory = Path(__file__).parent.resolve()
sys.path.insert(0, f"{parent_directory}/..")

# Import function to be tested
from src.list_concat import concat_list 
# Import unittest module
import unittest
class TestContactList(unittest.TestCase):
    def test_empty_list(self):
        """Test with empty list input"""
        result = concat_list([])
        self.assertEqual(result, "")

    def test_normal_case(self):
        """Test with normal input list"""
        words = ["yoda", "best", "has"]
        result = concat_list(words)
        self.assertEqual(result, "yes")

    def test_single_word(self):
        """Test with single word in list"""
        words = ["hello"]
        result = concat_list(words)
        self.assertEqual(result, "h")

    def test_different_length_words(self):
        """Test with words of different lengths"""
        words = ["cat", "python", "go"]
        result = concat_list(words)
        self.assertEqual(result, "cyg")

    def test_numbers_in_words(self):
        """Test with strings containing numbers"""
        words = ["h1", "a2", "t3"]
        result = concat_list(words)
        self.assertEqual(result, "h2t")

    def test_special_characters(self):
        """Test with special characters"""
        words = ["@bc", "#de", "$fg"]
        result = concat_list(words)
        self.assertEqual(result, "@dg")

    def test_spaces_in_words(self):
        """Test with words containing spaces"""
        words = ["a b", "c d", "e f"]
        result = concat_list(words)
        self.assertEqual(result, "a f")

    def test_unicode_characters(self):
        """Test with unicode characters"""
        words = ["über", "café", "señor"]
        result = concat_list(words)
        self.assertEqual(result, "üañ")

if __name__ == '__main__':
    unittest.main()

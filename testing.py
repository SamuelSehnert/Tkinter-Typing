import unittest
from main import *

class TestList(unittest.TestCase):
    def test_01(self):
        self.assertEqual(calculate_score("hllo!", "hello!"), "83.33%")
        self.assertEqual(calculate_score("hll!", "hello!"), "66.67%")
        self.assertEqual(calculate_score("ello!", "hello!"), "83.33%")
        self.assertEqual(calculate_score("hll!", "hello!"), "66.67%")
        self.assertEqual(calculate_score("!", "hello!"), "16.67%")
        self.assertEqual(calculate_score("h", "hello!"), "16.67%")
        self.assertEqual(calculate_score("l", "hello!"), "16.67%")
    
    def test_02(self):
        self.assertEqual(calculate_score("heello!", "hello!"), "83.33%")
        self.assertEqual(calculate_score("Joe iss Awesome!", "Joe is Awesome!"), "93.33%")
        self.assertEqual(calculate_score("hhello!!", "hello!"), "66.67%")
        self.assertEqual(calculate_score("Pythion", "Python"), "83.33%")

    def test_03(self):
        self.assertEqual(calculate_score("hello!", "hello!"), "100.0%")
        self.assertEqual(calculate_score("My friend is nice?", "My friend is nice?"), "100.0%")
        self.assertEqual(calculate_score("hello", "Always test programs!"), "0.0%")

if __name__ == "__main__":
    unittest.main()

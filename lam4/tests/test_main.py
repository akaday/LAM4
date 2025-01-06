import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from src.main import sample_function

class TestSampleFunction(unittest.TestCase):
    def test_sample_function(self):
        self.assertEqual(sample_function(2, 3), 5)
        self.assertEqual(sample_function(-1, 1), 0)
        self.assertEqual(sample_function(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

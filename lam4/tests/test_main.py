import sys
import os

# Add the src directory to the Python path explicitly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import sample_function

import unittest

class TestSampleFunction(unittest.TestCase):
    def test_sample_function(self):
        self.assertEqual(sample_function(2, 3), 5)
        self.assertEqual(sample_function(-1, 1), 0)
        self.assertEqual(sample_function(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

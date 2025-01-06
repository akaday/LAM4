import unittest
from lam4.src.main import optimize_code

class TestOptimizeCode(unittest.TestCase):
    def test_optimize_code(self):
        code = """
        def example_function():
            result = redundant_computation()
            return result
        """
        optimized_code = optimize_code(code)
        expected_code = """
        def example_function():
            return result
        """
        self.assertEqual(optimized_code.strip(), expected_code.strip())

if __name__ == '__main__':
    unittest.main()

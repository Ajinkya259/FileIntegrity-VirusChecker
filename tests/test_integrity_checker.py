import unittest
from src.integrity_checker import IntegrityChecker

class TestIntegrityChecker(unittest.TestCase):
    def setUp(self):
        self.checker = IntegrityChecker()

    def test_calculate_checksum(self):
        test_file = "examples/test_file.txt"
        expected_checksum = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  
        actual_checksum = self.checker.calculate_checksum(test_file)
        self.assertEqual(expected_checksum, actual_checksum)

if __name__ == "__main__":
    unittest.main()

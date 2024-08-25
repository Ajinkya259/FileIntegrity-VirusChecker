import unittest
from src.file_selector import FileSelector
import os

class TestFileSelector(unittest.TestCase):
    def setUp(self):
        self.selector = FileSelector()

    def test_select_files(self):
        test_dir = "examples"
        os.makedirs(test_dir, exist_ok=True)
        with open(os.path.join(test_dir, "test_file.txt"), "w") as f:
            f.write("")

        files = self.selector.select_files()
        self.assertIn(os.path.join(test_dir, "test_file.txt"), files)

if __name__ == "__main__":
    unittest.main()

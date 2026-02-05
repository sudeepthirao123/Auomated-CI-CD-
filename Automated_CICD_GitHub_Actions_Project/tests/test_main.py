
import unittest
from app.main import main

class TestMain(unittest.TestCase):
    def test_run(self):
        self.assertIsNone(main())

if __name__ == "__main__":
    unittest.main()

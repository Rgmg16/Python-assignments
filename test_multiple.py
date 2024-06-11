from multiple import multiply
import unittest

class test_multiple(unittest.TestCase):
    def test_multiple(self):
        self.assertEqual(multiply(2,3),6)
        
unittest.main()        
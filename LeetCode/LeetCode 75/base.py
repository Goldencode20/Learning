import unittest

class Solution(unittest.TestCase):

    def problem(self):
        return True

    def test(self):
        self.assertEqual(self.problem(), True)
        self.assertEqual(self.problem(), True)

if __name__ == '__main__':
    unittest.main()
import unittest

class Solution(unittest.TestCase):

    def problem(self):
        return True

    def test_isSubsequence(self):
        self.assertEqual(self.problem(), True)
        self.assertEqual(self.problem(), False)
        self.assertEqual(self.problem(), False)

if __name__ == '__main__':
    unittest.main()
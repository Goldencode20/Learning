import unittest

class Solution(unittest.TestCase):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) > len(t)):
            return False
        tPointer = 0
        if(len(s) == 0):
            return True
        for c1 in t:
            if(c1 == s[tPointer]):
                tPointer += 1
                if(tPointer >= len(s)):
                    return True
        
        return False

    def test_isSubsequence(self):
        self.assertEqual(self.isSubsequence("abc", "ahbgdc"), True)
        self.assertEqual(self.isSubsequence("axc", "ahbgdc"), False)
        self.assertEqual(self.isSubsequence("abcefgi", "ahbgdc"), False)

if __name__ == '__main__':
    unittest.main()
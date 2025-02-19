import unittest

class Solution(unittest.TestCase):

    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        
        numChars1 = {}
        numChars2 = {}

        for c in word1:
            numChars1[c] = numChars1.get(c, 0) + 1

        for c in word2:
            numChars2[c] = numChars2.get(c, 0) + 1
        
        if set(numChars1.keys()) != set(numChars2.keys()):
            return False
        
        numDiffChars1 = {}
        numDiffChars2 = {}

        for val in numChars1.values():
            numDiffChars1[val] = numDiffChars1.get(val, 0) + 1

        for val in numChars2.values():
            numDiffChars2[val] = numDiffChars2.get(val, 0) + 1

        return numDiffChars1 == numDiffChars2

    def test(self):
        self.assertEqual(self.closeStrings("abc", "bca"), True)
        self.assertEqual(self.closeStrings("a", "aa"), False)
        self.assertEqual(self.closeStrings("cabbba", "abbccc"), False)

if __name__ == '__main__':
    unittest.main()
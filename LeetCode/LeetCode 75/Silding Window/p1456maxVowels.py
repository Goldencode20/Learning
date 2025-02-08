import unittest

class Solution(unittest.TestCase):

    def isVowel(self, x): 
        if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'): 
            return True
        else: 
            return False
    
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        right = 0
        left = 0 - k
        count = 0
        maxCount = 0
        while right < len(s):
            if (left >= 0):
                if (Solution.isVowel(self, s[left])):
                    count -= 1
            if (Solution.isVowel(self, s[right])):
                count += 1
                if (count > maxCount):
                    maxCount = count
                    if maxCount == k:
                        return maxCount
            left += 1
            right += 1
           
        return maxCount

    def test(self):
        self.assertEqual(self.maxVowels("abciiidef", 3), 3)
        self.assertEqual(self.maxVowels("aeiou", 2), 2)
        self.assertEqual(self.maxVowels("leetcode", 3), 2)

if __name__ == '__main__':
    unittest.main()
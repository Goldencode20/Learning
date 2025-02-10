import unittest

class Solution(unittest.TestCase):

    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zeroCount = 0
        maxCount = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            if (right - left + 1) > maxCount:
                maxCount = right - left + 1
        return maxCount

    def test(self):
        self.assertEqual(self.longestOnes([1,0,1], 2), 3)
        self.assertEqual(self.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2), 6)
        self.assertEqual(self.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10)

if __name__ == '__main__':
    unittest.main()
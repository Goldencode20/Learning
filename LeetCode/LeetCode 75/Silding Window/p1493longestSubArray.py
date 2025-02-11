import unittest

class Solution(unittest.TestCase):

    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        zeros = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == len(nums) else ans
        

    def test(self):
        self.assertEqual(self.longestSubarray([1,1,0,1]), 3)
        self.assertEqual(self.longestSubarray([0,1,1,1,0,1,1,0,1]), 5)
        self.assertEqual(self.longestSubarray([1,1,1]), 2)

if __name__ == '__main__':
    unittest.main()
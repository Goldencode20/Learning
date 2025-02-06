import unittest

class Solution(unittest.TestCase):

    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        nums.sort()
        left = 0
        right = len(nums) - 1

        while (left != right and left < right):
            if (nums[left] + nums[right] == k):
                count += 1
                left += 1
                right -= 1
            elif (nums[left] + nums[right] >= k):
                right -= 1
            else:
                left += 1
                
        #print(nums)
        return count

    def test_isSubsequence(self):
        self.assertEqual(self.maxOperations([1,2,3,4], 5), 1)
        self.assertEqual(self.maxOperations([3,1,3,4,3], 6), 2)

if __name__ == '__main__':
    unittest.main()
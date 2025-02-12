import unittest

class Solution(unittest.TestCase):

    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rightSum = sum(nums) - nums[0]
        leftSum = 0
        temp = nums[0]

        for i in range(1, len(nums)):
            if(leftSum == rightSum):
                return i - 1

            leftSum += temp
            temp = nums[i]
            rightSum -= nums[i]

        if(leftSum == rightSum):
            return len(nums) - 1
        
        return -1


    def test(self):
        self.assertEqual(self.pivotIndex([1,7,3,6,5,6]), 3)
        self.assertEqual(self.pivotIndex([1,2,3]), -1)
        self.assertEqual(self.pivotIndex([2,1,-1]), 0)
        self.assertEqual(self.pivotIndex([-1,-1,0,1,1,0]), 5)

if __name__ == '__main__':
    unittest.main()
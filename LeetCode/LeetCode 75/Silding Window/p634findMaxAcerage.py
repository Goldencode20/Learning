import unittest

class Solution(unittest.TestCase):

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        count = 0 - k
        maxAverage = float('-inf')
        total = 0
        for num in nums:   
            total += num
            count += 1
            #print(sum)
            if(count >= 0):
                if (float(total) / k) > maxAverage:
                    maxAverage = float(total) / k
                total -= nums[count]
            #print(maxAverage)
        return maxAverage

    def test_findMaxAverage(self):
        self.assertEqual(self.findMaxAverage([1,12,-5,-6,50,3], 4), 12.75000)
        self.assertEqual(self.findMaxAverage([5], 1), 5.00000)
        self.assertEqual(self.findMaxAverage([1,0,1,4,2], 4), 1.75000)

if __name__ == '__main__':
    unittest.main()
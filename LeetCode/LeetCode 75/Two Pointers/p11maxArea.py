import unittest

class Solution(unittest.TestCase):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def test_isSubsequence(self):
        self.assertEqual(self.maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(self.maxArea([1,1]), 1)

if __name__ == '__main__':
    unittest.main()
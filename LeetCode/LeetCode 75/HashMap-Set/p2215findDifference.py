import unittest

class Solution(unittest.TestCase):

    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        unique1 = set(nums1)
        unique2 = set(nums2)

        removeLst = []

        for num in unique1:
            if num in unique2:
                removeLst.append(num)
        
        for num in removeLst:
            unique1.remove(num)
            unique2.remove(num)

        return [list(unique1), list(unique2)]
    
    def test(self):
        self.assertEqual(self.findDifference([1,2,3], [2,4,6]), [[1,3],[4,6]])
        self.assertEqual(self.findDifference([1,2,3,3], [1,1,2,2]), [[3],[]])

if __name__ == '__main__':
    unittest.main()
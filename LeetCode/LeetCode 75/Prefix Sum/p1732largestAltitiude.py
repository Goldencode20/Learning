import unittest

class Solution(unittest.TestCase):

    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = 0
        total = 0

        for num in gain:
            total += num
            highest = max(highest, total)

        return highest

    def test(self):
        self.assertEqual(self.largestAltitude([-5,1,5,0,-7]), 1)
        self.assertEqual(self.largestAltitude([-4,-3,-2,-1,4,3,2]), 0
        )

if __name__ == '__main__':
    unittest.main()
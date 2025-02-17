import unittest

class Solution(unittest.TestCase):

    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        map_count = {}
        
        for num in arr:
            if num in map_count:
                map_count[num] += 1
            else:
                map_count[num] = 1

        count_set = set()

        for key in map_count:
            if map_count[key] in count_set:
                return False
            else:
                count_set.add(map_count[key])
        
        return True


    def test(self):
        self.assertEqual(self.uniqueOccurrences([1,2,2,1,1,3]), True)
        self.assertEqual(self.uniqueOccurrences([1,2]), False)
        self.assertEqual(self.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]), True)


if __name__ == '__main__':
    unittest.main()
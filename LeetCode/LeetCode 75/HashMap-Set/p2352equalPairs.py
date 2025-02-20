import unittest

class Solution(unittest.TestCase):

    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = {}
        cols = {}

        for row in grid:
            row = tuple(row)
            rows[row] = rows.get(row, 0) + 1
        
        grid = (zip(*grid))

        for col in grid:
            col = tuple(col)
            cols[col] = cols.get(col, 0) + 1

        total = 0

        for key in rows:
            if key in cols:
                total += rows[key] * cols[key]

        return total

    def test(self):
        self.assertEqual(self.equalPairs([[3,2,1],[1,7,6],[2,7,7]]), 1)
        self.assertEqual(self.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]), 3)

if __name__ == '__main__':
    unittest.main()
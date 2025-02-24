import unittest

class Solution(unittest.TestCase):

    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []

        for a in asteroids:

            while res and a < 0 < res[-1]:
                if -a > res[-1]:
                    res.pop()
                    continue
                elif -a == res[-1]:
                    res.pop()
                break
            else:
                res.append(a)

        return res

    def test(self):
        self.assertEqual(self.asteroidCollision([5,10,-5]), [5,10])
        self.assertEqual(self.asteroidCollision([8,-8]), [])
        self.assertEqual(self.asteroidCollision([10,2,-5]), ([10]))
        self.assertEqual(self.asteroidCollision([2,5,10,-1000]), ([-1000]))
        self.assertEqual(self.asteroidCollision([-2,-1,1,2]), [-2,-1,1,2])
        self.assertEqual(self.asteroidCollision([-2,-2,-2,-2]), [-2,-2,-2,-2])

if __name__ == '__main__':
    unittest.main()
import unittest

class Solution(unittest.TestCase):

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant = []
        dire = []
        
        for i, vote in enumerate(senate):
            if vote == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        n = len(senate)

        while (len(radiant) != 0) and (len(dire) != 0):
            n += 1
            if radiant[0] < dire[0]:
                radiant.append(n)
            else:
                dire.append(n)
            
            radiant.pop(0)
            dire.pop(0)
        
        if radiant:
            return "Radiant"
        
        return "Dire"

    def test(self):
        self.assertEqual(self.predictPartyVictory("RD"), "Radiant")
        self.assertEqual(self.predictPartyVictory("RDD"), "Dire")

if __name__ == '__main__':
    unittest.main()
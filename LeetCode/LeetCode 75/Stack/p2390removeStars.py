import unittest

class Solution(unittest.TestCase):

    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_stack = list()
        for c in s:
            if char_stack and c == '*':
                char_stack.pop()
            elif c != '*':
                char_stack.append(c)

        output = ""

        char_stack.reverse()

        while char_stack:
            output += char_stack.pop()

        return output

    def test(self):
        self.assertEqual(self.removeStars("leet**cod*e"), "lecoe")
        self.assertEqual(self.removeStars("erase*****"), "")

if __name__ == '__main__':
    unittest.main()
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # Length must be same
        if len(s) != len(goal):
            return False

        return goal in (s + s)
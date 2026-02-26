class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(cost)
        
        # Base cases
        prev2 = cost[0]   # cost to reach step 0
        prev1 = cost[1]   # cost to reach step 1
        
        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
        
        # We can end from either last step or second last step
        return min(prev1, prev2)
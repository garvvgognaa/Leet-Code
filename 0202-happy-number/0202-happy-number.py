class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def nextNumber(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        slow = n
        fast = nextNumber(n)
        
        while fast != 1 and slow != fast:
            slow = nextNumber(slow)
            fast = nextNumber(nextNumber(fast))
        
        return fast == 1

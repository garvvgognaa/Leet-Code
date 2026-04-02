class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y
        count = 0
        
        while xor:
            count += xor & 1   # check last bit
            xor = xor >> 1     # shift right
        
        return count
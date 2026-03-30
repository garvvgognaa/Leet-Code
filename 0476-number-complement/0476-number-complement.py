class Solution(object):
    def findComplement(self, num):
        binary = bin(num)[2:]  # remove '0b'
        
        complement = ""
        for bit in binary:
            if bit == '0':
                complement += '1'
            else:
                complement += '0'
        
        return int(complement, 2)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1,numRows+1):
            res.append([1]*i)

        for i in range(2,numRows):
            n = len(res[i])
            for j in range(i-1):
                res[i][n-i+j] = res[i-1][j] + res[i-1][j+1]
        
        return res

            

        
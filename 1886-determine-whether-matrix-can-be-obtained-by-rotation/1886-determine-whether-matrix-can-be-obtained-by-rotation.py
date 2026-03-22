class Solution(object):
    def findRotation(self, mat, target):
        def rotate(matrix):
            n = len(matrix)
            # rotate 90° clockwise
            return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
        
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False
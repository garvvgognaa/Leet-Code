class Solution(object):
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        # If total is odd → impossible
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # 🔹 Check horizontal cuts
        curr = 0
        for i in range(m - 1):  # cut after row i
            curr += sum(grid[i])
            if curr == target:
                return True
        
        # 🔹 Check vertical cuts
        col_sum = [0] * n
        for i in range(m):
            for j in range(n):
                col_sum[j] += grid[i][j]
        
        curr = 0
        for j in range(n - 1):  # cut after column j
            curr += col_sum[j]
            if curr == target:
                return True
        
        return False
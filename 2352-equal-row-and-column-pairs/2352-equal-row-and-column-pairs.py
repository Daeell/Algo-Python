class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if all(grid[i][k] == grid[k][j] for k in range(n)):
                    cnt += 1
        return cnt
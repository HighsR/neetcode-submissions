class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n==0 and m==0:
            return 1
        row = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                row[j] = row[j] + row[j-1]
        return row[n-1]
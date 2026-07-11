class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        tbl = [0] * (n+1)
        tbl[0] = 1
        tbl[1] = 1

        for i in range(2, n+1):
            tbl[i] = tbl[i-1] + tbl[i-2]
        
        return tbl[n]
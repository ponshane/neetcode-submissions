class Solution:

    # memorization solution; time complexity: O(n)
    def dp_with_mem(self, n, mem):
        # base case
        if n <= 2:
            return n
        
        if n in mem:
            return mem[n]

        res = self.dp_with_mem(n-1, mem) + self.dp_with_mem(n-2, mem)
        mem[n] = res

        return res

    def climbStairs(self, n: int) -> int:
        mem = {}
        res = self.dp_with_mem(n, mem)
        return res    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return # terminate so we can go back to call stack
            
            # include
            subset.append(nums[i])
            dfs(i + 1)

            # exclude
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
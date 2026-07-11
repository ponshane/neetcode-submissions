class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            
            # base condition
            if total == target:
                res.append(cur.copy())
                return
            
            # terminate condition
            if i == len(nums) or total > target:
                return

            # include
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # backtracking
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)

        return res
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        res = 1000

        while l <= r:
            
            # if the window is sorted
            # we check the left-most one bc it could be minimum candidate
            if nums[l] < nums[r]:
                return min(res, nums[l])

            mid = l + (r-l) // 2
            res = min(res, nums[mid])
            
            # since nums[l] > nums[r], this is a rotated array
            # nums[l] <= nums[mid] means the window from l to mid is in rotated part
            # we should move to unrotated part 
            if nums[l] <= nums[mid]: # TRICK
                l = mid + 1
            else:
                r = mid - 1   

        return res
            
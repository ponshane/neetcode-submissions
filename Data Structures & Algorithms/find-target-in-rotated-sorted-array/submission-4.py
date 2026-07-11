class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            
            m = l + (r-l) // 2
            
            # check if m position is the target
            if nums[m] == target:
                return m

            # evaluate if left part is rotated array
            # note: <= condition is set for 2 elements case
            if nums[l] <= nums[m]:
                # we already check nums[m] == target
                # target could be at left-bounding
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # check right part
            else:
                # target could be at right-bounding
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1
                

        
            

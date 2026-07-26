class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] >= nums[0] and target < nums[0]:
                # We're in left sorted array
                # But target is in right sorted array 
                left = mid + 1
            elif nums[mid] < nums[0] and target >= nums[0]:
                # We're in right sorted array
                # But target is in left sorted array 
                right = mid - 1
            # Otherwise: Normal binary search
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
            
        return -1
        
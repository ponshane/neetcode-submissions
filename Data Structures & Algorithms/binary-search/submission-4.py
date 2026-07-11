class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums)
        mid = (head + tail) // 2

        while (head <= tail) and (mid < len(nums)):
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                head = mid + 1
            elif target < nums[mid]:
                tail = mid - 1
            mid = (head + tail) // 2
        return -1
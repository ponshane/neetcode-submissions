class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1

        while head <= tail:
            mid = head + (tail-head)//2

            if nums[mid] > target:
                tail = mid - 1
            elif nums[mid] < target:
                head = mid + 1
            else:
                return mid

        return -1
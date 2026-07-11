class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in value_index_dict:
                j = value_index_dict[difference]
                return sorted([i, j])
            else:
                value_index_dict[nums[i]] = i

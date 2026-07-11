class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearance = set()
        for i in nums:
            if i in appearance:
                return True
            elif i not in appearance:
                appearance.add(i)
        return False
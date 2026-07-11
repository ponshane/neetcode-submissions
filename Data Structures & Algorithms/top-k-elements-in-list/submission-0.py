class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums))]
        
        for num, cnt in count_dict.items():
            buckets[cnt-1].append(num)

        ans = []
        for i in range(len(buckets)-1, -1, -1):
            ans += buckets[i]
            if len(ans) >= k:
                return ans[:k]
            


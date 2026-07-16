class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1
        
        cnt_bucket = [[] for _ in range(len(nums)+1)]
        for key, cnt in count_dict.items():
            cnt_bucket[cnt].append(key)
        
        res = []
        for i in range(len(cnt_bucket)-1, -1, -1):
            res += cnt_bucket[i]
            if len(res) >= k:
                break
        return res[:k]

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_k = 1
        max_k = max(piles)
        k_candidate = max_k

        while min_k <= max_k:

            m = min_k + (max_k - min_k) // 2

            required_h = sum([math.ceil(x/m) for x in piles])

            if required_h > h: # if m is too small
                min_k = m + 1
            else: # if m is valid, we try searching smaller one
                k_candidate = min(k_candidate, m)
                max_k = m - 1
        
        return k_candidate
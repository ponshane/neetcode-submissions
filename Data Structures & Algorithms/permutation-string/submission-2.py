class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        target_freq = {}
        for c in s1:
            target_freq[c] = 1 + target_freq.get(c, 0)
        
        size_of_window = len(s1)

        for i in range(0, len(s2)):
            sub_s2 = s2[i:i+size_of_window]
            current_freq = {}
            for c in sub_s2:
                current_freq[c] = 1 + current_freq.get(c, 0)

            if target_freq == current_freq:
                return True

        return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # Frequency arrays for lowercase 'a'-'z'
        s1_count = [0] * 26
        window_count = [0] * 26

        # 1. Fill s1_count and the first window of s2
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # 2. Slide the window across s2
        # We start from index n1 because we already processed 0 to n1-1
        for i in range(n1, n2):
            # Check if current window matches
            if s1_count == window_count:
                return True
            
            # Slide: Add the new character on the right
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # Slide: Remove the character that is no longer in the window
            window_count[ord(s2[i - n1]) - ord('a')] -= 1

        # Check the very last window after the loop ends
        return s1_count == window_count
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars_dict = dict()
        for s_char in s:
            if s_char in s_chars_dict:
                s_chars_dict[s_char] += 1
            else:
                s_chars_dict[s_char] = 0
        
        t_chars_dict = dict()
        for t_char in t:
            if t_char in t_chars_dict:
                t_chars_dict[t_char] += 1
            else:
                t_chars_dict[t_char] = 0

        if s_chars_dict == t_chars_dict:
            return True
        else:
            return False
        
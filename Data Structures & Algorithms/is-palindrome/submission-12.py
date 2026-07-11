class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        forward_index = 0
        backward_index = len(s) - 1
        #first_half = ""
        #second_half = ""
        
        while forward_index < backward_index:
            
            # fc = s[forward_index]
            while (not s[forward_index].isalnum()) and (forward_index < backward_index):
                forward_index += 1
                # fc = s[forward_index]
            
            #if fc.isalnum():
            #    first_half += fc
            #    forward_index += 1

            # sc = s[backward_index]
            while (not s[backward_index].isalnum()) and (backward_index > forward_index):
                backward_index -= 1
                # sc = s[backward_index]
            
            #if sc.isalnum():
            #    second_half += sc
            #    backward_index -= 1
            fc = s[forward_index]
            sc = s[backward_index]
            if fc != sc:
                return False

            forward_index += 1
            backward_index -= 1
        
        return True
        #if first_half == second_half:
        #    return True
        #else:
        #    return False
            
            
class Solution:
    def isValid(self, s: str) -> bool:

        close_bracket_dict = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []
        for c in s:
            
            if c not in close_bracket_dict:
                stack.append(c)
            else:

                # control the case starting with close brackets, e.g., ], }, )
                elem = ""
                if len(stack) > 0:
                    elem = stack.pop()
                
                if elem != close_bracket_dict[c]:
                    return False

        # check if there is any open brackets left
        if len(stack) == 0:
            return True
        else:
            return False

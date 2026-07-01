class Solution:
    def isValid(self, s: str) -> bool:
        # Use stack
        # Push to stack 
        # Pop when see closing and if it matches
        # For an opening bracket, push it onto the stack. 
        # If the bracket is a closing type, check for the corresponding opening bracket at the 
        # top of the stack.
        # Order important here ()[] - true vs ([)] -> false
        # First case - not start with closing paranthesis, 
        # also closing needs to come for first one before next close one

        d_map = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = []
        for ch in s:
            if ch in d_map.keys():
                stack.append(ch)
            else:
                if not stack: # nothing to match ex. "["
                    return False
                ch_validate = stack.pop() # remove from start of the list
                if d_map[ch_validate] != ch:
                    return False
        return stack == []

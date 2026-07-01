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

        close_to_open_map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for ch in s:
            if ch in close_to_open_map:
                # Match closing braces
                if stack and stack[-1] == close_to_open_map[ch]: # Closing brace match the last opening brace
                    stack.pop()
                else:
                    return False # nothing to match ex. "["
            else:
                stack.append(ch) # Append opening braces
        return stack == []

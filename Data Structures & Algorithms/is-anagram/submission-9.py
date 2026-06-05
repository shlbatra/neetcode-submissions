class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # String anagram
        # Both strings have same character so initial same length 
        # Keep a dictionary based on s and t
        # If both dictionaries align then true else false
        # time -> O(n+m), space -> O(n+m)
        if len(s) != len(t):
            return False
        
        a_s = [0] * 26 # length of 26 for 26 characters - keep count of characters +/-1

        # Use array instead of hashmap
        for i in range(len(s)): # as both same length
            a_s[ord(s[i])-ord('a')] += 1
            a_s[ord(t[i])-ord('a')] -= 1
        
        for element in a_s:
            if element != 0:
                return False
        return True
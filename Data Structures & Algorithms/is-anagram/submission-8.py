class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # String anagram
        # Both strings have same character so initial same length 
        # Keep a dictionary based on s and t
        # If both dictionaries align then true else false
        # time -> O(n+m), space -> O(n+m)
        if len(s) != len(t):
            return False
        
        d_s = {}
        d_t = {}

        for i in range(len(s)): # as both same length
            d_s[s[i]] = d_s.get(s[i], 0) + 1
            d_t[t[i]] = d_t.get(t[i], 0) + 1
        
        return d_s == d_t
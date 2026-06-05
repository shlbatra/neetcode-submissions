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

        for ch in s:
            d_s[ch] = d_s.get(ch, 0) + 1
        for ch in t:
            d_t[ch] = d_t.get(ch, 0) + 1
        
        for ch,num_ch in d_s.items():
                if d_t.get(ch, 0) != d_s.get(ch, 0):
                    return False
        return True 
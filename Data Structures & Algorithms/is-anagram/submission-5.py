class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}

        if len(s) != len(t):
            return False

        for ch in s:
            h1[ch] = h1.get(ch, 0) + 1

        for ch in t:
            h2[ch] = h2.get(ch, 0) + 1

        for c in h1:
            if h1[c] != h2.get(c, 0): 
                return False
        
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}

        for ch in s:
            h1[ch] = h1.get(ch, 0) + 1

        for ch in t:
            h2[ch] = h2.get(ch, 0) + 1

        if h1 == h2:
            return True
        else:
            return False
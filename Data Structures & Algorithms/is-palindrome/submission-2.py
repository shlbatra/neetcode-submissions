class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        while l < r:

            # Skip non alpha numeric below -
            while l < r and not self.alphaNum(s[l]):
                l = l + 1
            while r > l and not self.alphaNum(s[r]):
                r = r - 1
            # Do comparison for alpha numeric
            if s[l].lower() != s[r].lower():
                return False
            # Keep moving after every loop
            l, r = l+1, r-1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
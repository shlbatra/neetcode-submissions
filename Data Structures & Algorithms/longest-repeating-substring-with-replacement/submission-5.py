from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Longest substring after replace max k chars
        # using 2 ptr - l and r
        # Solve using O(26.n)
        # In window, replace less frequent character with most common character
        # Hash map {char: occ} in that window
        # WindowLen - Count of most freq char -> # of chars to be replaced to match most freq char <=k - current window valid
        # Add sliding window technique - expand until above condition match
        # if condition not match -> move left till condition met above

        l, r = 0, 0
        maxf = 0
        w_set = set()
        for ch in s:
            w_set.add(ch)

        res = 0
        # abab.  set -> (a, b) 
        # a 1, 
        for c in w_set:
            l, cnt = 0, 0
            for r in range(len(s)):
                if s[r] == c: # Keep incrementing counter when c matches
                    cnt += 1

                while (r-l+1) - cnt > k: # if window - common occ > k then need to move left counter
                    if s[l] == c: # If left counter same as character, update count
                        cnt -= 1
                    l += 1 # Increment left counter
                res = max(res, r-l+1) 
        return res

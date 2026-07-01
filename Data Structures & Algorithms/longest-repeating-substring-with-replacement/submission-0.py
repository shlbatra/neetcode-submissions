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
        w_dict = defaultdict(int)
        res = 0
        for r in range(len(s)):
            w_dict[s[r]] += 1
            maxf = max(maxf, w_dict[s[r]])
            while (r-l+1) - maxf > k:
                w_dict[s[l]] -= 1
                l = l + 1
            res = max(res, r-l+1)
        return res

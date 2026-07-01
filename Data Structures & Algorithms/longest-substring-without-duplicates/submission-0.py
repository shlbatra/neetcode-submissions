class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Longest substring without repeating characters
        # Iterate over each windows from i, and keep duplicates in a set
        # Keep count of max window
        # Option2: Left at start of substring and right pointer at end of substring
        # Set to keep unique elements in substring
        # abcabcbb
        # initial abc, when next a, remove l until no duplicate and add r until no duplicate
        duplicate_set = set()
        res = 0
        l, r = 0, 0
        for r in range(len(s)):
            while s[r] in duplicate_set: # shrink when right in window
                duplicate_set.remove(s[l])
                l = l + 1
            # default keep adding r to set and incrementing r and recalculating window 
            duplicate_set.add(s[r])
            curr_window = r-l+1
            res = max(curr_window, res)

        return res
            

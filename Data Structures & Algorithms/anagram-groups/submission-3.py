class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group strings together -> same character length

        # if only 1 element then return that

        # Approach 1
        # Sort all strings
        # All sorted strings same -> palindrome
        # Time complexity O(m*nlogn) -> m elements and n avg elements per string

        # Better approach
        # dictionary with count of 26 chars as key -> mapped to substring
        # Time complexity O(n*m*26) and space complexity -> O(n)
        if len(strs) <= 1:
            return [strs]
        res = []
        
        d_str = defaultdict(list)    # [1a 1c 1t] -> ["cat", "act"]
        for word in strs:
            c_arr = [0] * 26
            for ch in word:
                c_arr[ord(ch)-ord('a')] += 1
            d_str[tuple(c_arr)].append(word)
        
        for c_arr, word_list in d_str.items():
            res.append(word_list)

        return res
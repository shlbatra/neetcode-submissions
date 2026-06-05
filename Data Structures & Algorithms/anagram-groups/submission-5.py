class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group strings together -> same character length

        # if only 1 element then return that

        # Approach 1
        # Sort all strings and put key as sorted string and list of string as values
        # All sorted strings same -> palindrome
        # Time complexity O(m*nlogn) -> m elements and n avg elements per string

        # Better approach
        # dictionary with count of 26 chars as key -> mapped to substring
        # Time complexity O(n*m*26) and space complexity -> O(n)
        if len(strs) <= 1:
            return [strs]
        res = defaultdict(list)
        
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        print(res)
        return list(res.values())
        
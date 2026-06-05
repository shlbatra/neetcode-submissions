class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Ex eat vs ate
        # [1e 1a 1t] vs [1a 1t 1e]

        h_map = defaultdict(list)

        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            h_map[tuple(count)].append(s)

        return list(h_map.values())

        
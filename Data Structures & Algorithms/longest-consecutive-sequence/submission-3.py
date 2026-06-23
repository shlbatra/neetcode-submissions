class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        # 4 [2, 3, 4, 5]

        # Approach1 - Sort nums, l and r ptr -> keep incrementing if 1 diff - get max sequence
        # O(nlogn) time complexity
        # Approach2 - O(n)
        # Beginning of Sequence - how start if number - 1 is not list of numbers
        if nums == []: return 0
        
        numSet = set(nums)
        longest = 1

        for num in numSet:
            if (num-1) not in numSet: # Start of sequence
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

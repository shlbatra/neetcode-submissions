class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        # 4 [2, 3, 4, 5]

        # Approach1 - Sort nums, l and r ptr -> keep incrementing if 1 diff - get max sequence
        # O(nlogn) time complexity
        # Approach2 - O(n)
        # Beginning of Sequence - how start if number - 1 is not list of numbers
        if nums == []: return 0
        
        nums = sorted(nums)
        streak = 1 # Start with single element
        max_streak = 1
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: # duplicate, skip
                continue
            elif nums[i] == nums[i-1] + 1: # consecutive
                print(nums[i-1])
                streak = streak + 1
                max_streak = max(streak, max_streak)
            else: # reset
                streak = 1
        print(max_streak)
        return max_streak
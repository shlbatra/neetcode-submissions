class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1, 2, 3, 4, 5]
        # Sorted and moved [3, 4, 5, 1, 2]
        # Binary search -> L and R -> return Left pointer for minimum on sorted array
        # One way - find pivot - elements not in increasing order 
        # l 3, r 2, m 5 based on binary search
        # rotated sorted array - one part sorted and other include rotation - need to find that
        # next how search - which region ?
        # Both sub array sorted, check Middle -> if left portion the go to right - as sorted and moved
        # If middle left portion - then check right (sorted) check if midde value >= num[l] then search right
        # if middle in right sorted portion - values on right greater then search on left
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            # Check if array already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            mid = int((l + r) / 2)
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                # Search right
                l = mid+1
            else:
                # Search left
                r = mid-1
        return res
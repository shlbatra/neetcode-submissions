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
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (r+l) // 2
            # If minimum is at mid itself - only time to check it
            if nums[mid] < nums[r]:
                # Search right
                r = mid # Min right of mid
            else:
                # Search left
                l = mid+1 # Min is at mid or left of it
        return nums[l]  # l == r points at the minimum
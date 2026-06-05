class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # difference of target - curr_num -> needs to be in array in another position
        # target - nums[i] = nums[j]
        # Loop through and difference with target - value -> is it part of remaining array ?
        # Use hashmap to store current index
        # 3, 4, 5, 6. - 7
        # h_map {3:0}
        # 0, 
        h_map = {} # {num:index}
        ans = []
        for i, num in enumerate(nums):
            if (target - num) in h_map:
                return ([h_map[target-num], i])
            h_map[num] = i
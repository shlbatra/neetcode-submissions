class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1,0,1,2,-1,-4]
        # [[-1,-1,2],[-1,0,1]]
        # Approach - Sort first. 
        # -4, -1, -1, 0, 1, 2 (skip duplicates when i move across sorted array) and also l & r window
        # then reduces to 2 sum using hash map or hash set
        # Or alternate left and right ptr sum > 0 then r shift left, sum < 0 then l shift right
        # soln O(nlogn) + O(n^2)
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):

            if i > 0 and nums[i-1] == nums[i]: # duplicate entries
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threesum = nums[i] + nums[l] + nums[r]

                if threesum > 0:
                    r = r - 1
                elif threesum < 0:
                    l = l + 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    r = r - 1
                    while nums[l] == nums[l-1] and l < r:
                        l = l + 1

        return res



            


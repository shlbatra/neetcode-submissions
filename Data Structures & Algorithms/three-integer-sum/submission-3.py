class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1,0,1,2,-1,-4]
        # [[-1,-1,2],[-1,0,1]]
        # Approach - Sort first. 
        # -4, -1, -1, 0, 1, 2 (skip duplicates when i move across sorted array) and also l & r window
        # then reduces to 2 sum using hash map or hash set
        # Or alternate left and right ptr sum > 0 then r shift left, sum < 0 then l shift right
        # soln O(nlogn) + O(n^2)
        # Next approach - use hashmap
        nums = sorted(nums)
        res = []
        c_map = defaultdict(int)
        
        for num in nums:
            c_map[num] += 1
        
        for i in range(len(nums)):

            if nums[i] > 0: # array already sorted so if minimum is > 0 then not possible to sum to 0
                break

            c_map[nums[i]] -= 1 # decrement current number

            if i > 0 and nums[i-1] == nums[i]: # duplicate entries
                continue

            for j in range(i+1, len(nums)):
                c_map[nums[j]] -= 1 # second number decrement

                if nums[j] == nums[j-1] and j - 1 > i: # skip duplicate for second number
                    continue

                third_number = 0 - nums[i] - nums[j]

                if c_map[third_number] > 0:
                    res.append([nums[i], nums[j], third_number])

            for j in range(i+1, len(nums)): 
                c_map[nums[j]] += 1

        return res



            


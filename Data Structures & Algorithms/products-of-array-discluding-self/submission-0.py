class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Given an integer array nums, return an array output 
        # where output[i] is the product of all the elements of nums except nums[i]
        # nums = [1,2,4,6]
        # [48,24,12,8]
        # Prefix -> [1, 2, 8, 48]
        # Postfix -> [48, 48, 24 ,6]
        # Approach 1 - product all and then divide by number in index - not allowed here
        # Approach 2 - Use Prefix * Postfix - both computed in O(n) and then iterate O(n) - Overall O(n)
        # Space - O(n) - memory - compute prefix and postfix store directly in output array
        # Prefix -> [1, 2, 8, 48]
        # Postfix -> [48, 48, 24 ,6]
        # [1*48, 1*24, 2*6, 8*1]
        prefix = 1
        output = [0] * len(nums)
        output[0] = 1
        for i in range(len(nums)-1):
            prefix = prefix * nums[i]
            output[i+1] = prefix
        print(output)
        postfix = 1
        for j in range(len(nums)-1, 0, -1):
            postfix = postfix * nums[j]
            output[j-1] = output[j-1] * postfix
        print(output)
        return output

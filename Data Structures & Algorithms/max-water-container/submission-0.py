class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointer solution
        # Given list of heights
        # formula to calculate area - (j-i) * min(heighti, heightj)
        # Move l and r ptrs -> 0 and len(num) - 1 to get initial maximum area with max width
        # Shift ptr which has lower height and it increases - then only move in direction with smaller ht
        # Keep max area to check
        # If values equal -> doesnt matter shift either or shift one where ht higher
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)

            if heights[l] >= heights[r]:
                r = r - 1
            else:
                l = l + 1

        return max_area

